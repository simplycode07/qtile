from libqtile import bar, widget
from libqtile.config import Screen
from libqtile.lazy import lazy
import random, os

random_pic = random.choice(os.listdir("/home/dhruv/Wallpapers/"))
max_title_length = 10

screens = [
    Screen(
        wallpaper="/home/dhruv/Wallpapers/"+random_pic,
        wallpaper_mode="fill",
        top=bar.Bar(
            [
                widget.Spacer(length=10),

                widget.CurrentLayout(padding=2),
                widget.GroupBox(inactive="#556ea6",
                                padding=4),

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
                                 padding=2,),

                widget.Spacer(length=10),
            ],
            20,
            opacity = 0.8,
            margin = [5, 5, 5, 5],

            border_width=[2, 2, 2, 2], 
            # border_color=["#7AA2F7", "00000000", "#7AA2F7", "00000000"]  
            # border_color=["#85caff", "#85caff", "#85caff", "#85caff"]
        ),

        x11_drag_polling_rate = 60,
    ),
]
