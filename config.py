from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from settings.keys import keys
import os, random, subprocess

mod = "mod4"
terminal = "kitty"
max_title_length = 0

random_pic = random.choice(os.listdir("/home/dhruv/Wallpapers/"))

groups=[Group("1"), Group("2"), Group("3")]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]
    )

layouts = [
    layout.Columns(border_focus=["#00000000", "#7AA2F7"], 
                   border_width=10,
                   lower_right=True),
    layout.Max(),
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    layout.MonadTall(),
    layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="sans",
    fontsize=16,
    padding=15,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        # lazy.screen.set_wallpaper("/home/dhruv/Wallpapers/pxfuel.jpg", mode="fill")
        wallpaper="/home/dhruv/Wallpapers/"+random_pic,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.CurrentLayout(padding=2),
                widget.GroupBox(padding=4),
                widget.Prompt(),
                widget.TaskList(icon_size=20,
                                border="00000000",
                                margin=0,
                                padding_y=0,
                                padding_x=5,
                                parse_text=lambda x: x[:max_title_length]+ "..." if len(x) > max_title_length else ""

                                ),

                widget.ThermalZone(padding=2, margin=2),

                widget.Clock(format="%d %h, %H:%M",
                             padding_x=2,
                             margin_x=2),

                widget.PulseVolume(fmt="󰓃 {}",
                                   step=2,
                                   padding=2),

                widget.Battery(format='{char} {percent:2.0%} {watt:.1f} W',
                               padding=2,
                               discharge_char = "",
                               charge_char = "󱐋",
                               empty_char = "∅"),

                widget.Backlight(backlight_name="amdgpu_bl0",
                                 change_command="brightnessctl set {0}%",
                                 step=5.2,
                                 padding=2),

                widget.QuickExit(default_text="[Exit]",
                                 countdown_format="[{} Sec]",
                                 padding=2),
            ],
            20,

            border_width=[2, 2, 2, 2], 
            border_color=["#7AA2F7", "00000000", "#7AA2F7", "00000000"]  
        ),
        right=bar.Gap(20),
        left=bar.Gap(20),

        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# lazy.screen.set_wallpaper("/home/dhruv/Wallpapers/pxfuel.jpg", mode="fill")
dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"

@hook.subscribe.startup_once
def autostart():
    script = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.Popen([script])


