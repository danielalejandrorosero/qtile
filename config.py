# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import subprocess
from libqtile import hook
from libqtile import bar, layout, qtile, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal


mod = "mod4"
terminal = guess_terminal()

colorBarra =  "#282a36"
dispositivo_red = ''
color_grupo1 = "#ff7f00"
color_grupo2 = "#d600f7"
color_grupo3 = "#007bff"
color_grupo4 = '#c60000'
def fc_rectangulo(vColor, tipo):
    if tipo == 0:
        icono = ""
    else:
        icono = ""
    return widget.TextBox(
        text=icono,
        fontsize=25,
        foreground=vColor,
        background="#282a36",
    )



def fc_icono(icono,color_grupo1):
    return widget.TextBox(
        text = icono,
        foreground = "#ffffff",
        background = color_grupo1,
        fontsize = 25
    )

keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # rofi 
    Key([mod], "Return", lazy.spawn('konsole'), desc="Launch terminal"),
    # Toggle between different layouts as defined below


    Key([mod], 'm', lazy.spawn("rofi -show drun "),desc="Abrir menu"),


    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
    #Key(
     #   [mod],
     #   "f",
     #   lazy.window.toggle_fullscreen(),
     #   desc="Toggle fullscreen on the focused window",
    #),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen on the focused window"),
    Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


groups = [Group(i) for i in  [
    "  " , "  " , "  " , "  ", 
]]

for i,group in enumerate(groups):
    numeroEscritorio = str(i+1)
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                numeroEscritorio,
                lazy.group[group.name].toscreen(),
                desc="Switch to group {}".format(group.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                numeroEscritorio,
                lazy.window.togroup(group.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(group.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused wind12ow to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

# este es el original
"""
groups = [Group(i) for i in  "123456789"]

for i in groups:
    keys.extend(
        [
            # mod1 + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    ) 
"""

layouts = [
    layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Ubuntu Mono Nerd Font",
    fontsize=13,
    padding=1,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(

        top=bar.Bar(
            [
                widget.GroupBox(
                    active="f1fa8c",
                    borderwidth = 1,
                    disable_drag = True,
                    fontsize = 26,
                    foreground = "#ffffff",
                    highlight_method = "block",
                    inactive = "#6272a4",  
                    margin_x = 0,
                    margin_y = 5,
                    other_current_screen_border = "#44475a", 
                    other_screen_border = "#44475a", 
                    padding_x = 0,
                    padding_y = 10,
                    this_current_screen_border="#bd93f9",
                    this_alert_method = "#bd93f9",
                    urgent_alert_method = "block",
                    urgent_border = "#ff5555",
                ),
                widget.Sep(
                    linewidth=0,
                    padding = 16,
                    foreground = "#ffffff",
                    background = "#282a36",
                    ),
                widget.Prompt(),
                widget.WindowName(
                    foreground = "#bd93f9",
                    background = "#282a36",
                ),
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                widget.Systray(
                    icon_size = 26,
                    background = "#282a36",
                ),
                widget.Sep(
                    linewidth=0,
                    padding = 16,
                    foreground = "#ffffff",
                    background = "#282a36",
                    ),
                fc_rectangulo(color_grupo1, 0),
                fc_icono("  ",color_grupo1),
                widget.ThermalSensor(
                    foreground = '#ffffff',
                    background = color_grupo1,
                    threshold = 50,
                    tag_sensor = "Core 0",
                    fmt = "T1:{}",
                    fontsize = 20,
                ),
                fc_icono('  ',color_grupo1),
                widget.Memory(
                    foreground = "#ffffff",
                    background = color_grupo1,
                ),
                fc_rectangulo(color_grupo1, 1),
                widget.Sep(
                    linewidth=0,
                    padding = 16,
                    foreground = "#ffffff",
                    background = "#282a36",
                    ),
                #grupo 2
                fc_rectangulo(color_grupo2, 0),
                fc_icono('  ',color_grupo2),
                widget.CheckUpdates(
                    background = color_grupo2,
                    colour_have_updates = "#bc0000",
                    colour_no_updates = "#ffffff",
                    no_update_string = '0',
                    display_format = '{updates}',
                    update_interval = 1800, 
                    distro = 'Arch_checkupdates',
                ),
                fc_icono('  ',color_grupo2),
                widget.Net(
                    foreground = "#ffffff",
                    background = color_grupo2,
                    format = '{down}   {up}',
                    interface = "wlan0",
                    use_bits = 'true'
                ),
                fc_rectangulo(color_grupo2, 1),
                widget.Sep(
                    linewidth=0,
                    padding = 16,
                    foreground = "#ffffff",
                    background = "#282a36",
                    ),
                fc_rectangulo(color_grupo3, 0),
                widget.Clock(
                    background = color_grupo3,
                    foreground = '#ffffff',
                    format="%d/%m/%Y %A %H:%M"),
                fc_rectangulo(color_grupo3, 1),
                widget.Sep(
                    linewidth=0,
                    padding = 16,
                    foreground = "#ffffff",
                    background = "#282a36",
                    ),
                fc_rectangulo(color_grupo4, 0),
                widget.CurrentLayoutIcon (
                    background = color_grupo4,
                    scale = 0.7
                ),
                widget.CurrentLayout(
                    background = color_grupo4,
                ),
                fc_rectangulo(color_grupo4, 1),
                widget.Sep(
                    linewidth=0,
                    padding = 16,
                    foreground = "#ffffff",
                    background = "#282a36",
                    ),
                widget.QuickExit(),
                widget.CurrentLayout(),
            ],
            25,
            background= colorBarra
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        # x11_drag_polling_rate = 60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

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




# este es la predeterminaa 
#@hook.subscribe.startup_once
#def autostart():
#    home = os.path.expanduser('~')
#    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    






@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    subprocess.Popen([home + '/.config/qtile/autostart.sh'])
    subprocess.Popen(["feh", "--bg-fill", "/home/daniel/Downloads/buenfondo.jpg"])



