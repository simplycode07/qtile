#!/bin/bash

state=$( xinput list-props 12 | grep "Device Enabled" | grep -o "[01]$" )
echo $state

if [ "$state" -eq '1' ];then
    xinput --disable 12 && echo "TouchPad Disabled" 
else
    xinput --enable 12 && echo "TouchPad Enabled"
fi
