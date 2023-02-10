 # -*- coding: utf-8 -*-
import os
import re
import socket
import subprocess
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen, DropDown, ScratchPad 
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from libqtile.dgroups import simple_key_binder
from libqtile.widget.image import Image
from libqtile.widget import Spacer, Backlight

import colors

#Variables
mod = "mod4"
mod1 = "mod1"
browser = 'google-chrome-stable'
terminal = 'kitty'
text_editor = 'code'
text_editor2 = terminal + ' nvim'
file_manager1 = 'dolphin'
file_manager2 = terminal + ' ranger'
file_launcher1 = 'rofi -show run'
file_launcher2 = 'dmenu_run'
# email_cliant = 'thunderbird'
process_viewer = terminal + ' htop'
configuration_menu = '.local/bin/rofi_configuration_menu'
website_menu = '.local/bin/rofi_website_menu'
colorscheme_menu = '.local/bin/rofi_colorscheme_menu'

mbfs = colors.mbfs()
doomOne = colors.doomOne()
dracula = colors.dracula()
everforest = colors.everforest()
nord = colors.nord()
gruvbox = colors.gruvbox()

#Choose colorscheme
colorscheme = dracula

#Colorschme funcstion
colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colorscheme 


#KEYBINDINGS

#Window keybindings
keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc = "Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc = "Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc = "Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc = "Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc = "Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc = "Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc = "Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc = "Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc = "Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc = "Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc = "Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc = "Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc = "Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "space", lazy.layout.toggle_split(),
        desc = "Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc = "Toggle between layouts"),
    
    # Close windows
    Key([mod, "shift"], "c", lazy.window.kill(), desc = "Kill focused window"),
    
    # Close, logout and reset Qtile
    Key([mod, "control"], "r", lazy.restart(), desc = "Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc = "Shutdown Qtile"),

    #Applications

    # Open Terminal
    Key([mod], "Return", lazy.spawn(terminal), desc = "Launch terminal"),
    
    #Browser
    Key([mod, "shift"], "b", lazy.spawn(browser), desc = "Launch browser"),

    #Text editor
    Key([mod, "shift"], "n", lazy.spawn(text_editor), desc = "Launch Neovim"),

    #Email cliant
    # Key([mod], "e", lazy.spawn(email_cliant), desc = "Launch thunderbird"),

    #File manager
    Key([mod, "shift"], "f", lazy.spawn(file_manager1), desc = "Lauch primary file manager"),

    #Rofi
    Key([mod, "shift"], "Return", lazy.spawn(file_launcher1), desc = "Launch primary launcher"),

    #Rofi Bash scripts
    # Key([mod], "d", lazy.spawn(file_launcher2), desc = "Launch secondary launcher"),
    Key([mod, "control"], "c", lazy.spawn(configuration_menu), desc = "Launch rofi configuration menu"),
    Key([mod, "control"], "b", lazy.spawn(website_menu), desc = "Launch rofi website menu"),
    Key([mod, "control"], "t", lazy.spawn(colorscheme_menu), desc = "Launch rofi colorscheme menu"),

    #Backup run launcher
    Key([mod], "r", lazy.spawncmd(), desc = "Spawn a command using a prompt widget"),

    # Hardware/system control
    #Sound
    Key([mod1], "v", lazy.spawn("pactl set-sink-volume 0 +5%")),
    Key([mod1, "shift"], "v", lazy.spawn("pactl set-sink-volume 0 -5%")),
    Key([], "XF86AudioMute", lazy.spawn("pactl set-sink-mute 0 toggle")),

    #Brightness
    Key([], "XF86MonBrightnessUp", lazy.spawn("lux -a 10%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("lux -s 10%")),
]

# keys = [
#          ### The essentials
#          Key([mod], "Return",
#              lazy.spawn(myTerm),
#              desc='Launches My Terminal'
#              ),
         
#         Key([mod, "shift"], "Return", lazy.spawn(file_launcher1), desc = "Launch primary launcher"),

#          Key([mod], "b",
#              lazy.spawn(myBrowser),
#              desc='Chrome browser'
#              ),
         
#          Key([mod, "shift"],"n",
#             lazy.spawn(text_editor2),
#             desc = "Launch Neovim"),            
         
#          Key([mod],"v",
#             lazy.spawn(text_editor),
#             desc = "Launch VSCode"),
#             #File manager
#          Key([mod, "shift"], "b",
#             lazy.spawn(file_manager1),
#             desc = "Lauch primary file manager"),
#          #Backup run launcher
#          Key([mod], "r", lazy.spawncmd(), desc = "Spawn a command using a prompt widget"),



#          # Key([mod], "/",
#          #     lazy.spawn("dtos-help"),
#          #     desc='DTOS Help'
#          #     ),
#          Key([mod], "Tab",
#              lazy.next_layout(),
#              desc='Toggle through layouts'
#              ),
#          Key([mod, "shift"], "c",
#              lazy.window.kill(),
#              desc='Kill active window'
#              ),
#          Key([mod, "shift"], "r",
#              lazy.restart(),
#              desc='Restart Qtile'
#              ),
#          Key([mod, "shift"], "q",
#              lazy.shutdown(),
#              desc='Shutdown Qtile'
#              ),
#          Key(["control", "shift"], "e",
#              lazy.spawn("emacsclient -c -a emacs"),
#              desc='Doom Emacs'
#              ),
#          ### Switch focus to specific monitor (out of three)
#          Key([mod], "w",
#              lazy.to_screen(0),
#              desc='Keyboard focus to monitor 1'
#              ),
#          Key([mod], "e",
#              lazy.to_screen(1),
#              desc='Keyboard focus to monitor 2'
#              ),
#          Key([mod], "r",
#              lazy.to_screen(2),
#              desc='Keyboard focus to monitor 3'
#              ),
#          ### Switch focus of monitors
#          Key([mod], "period",
#              lazy.next_screen(),
#              desc='Move focus to next monitor'
#              ),
#          Key([mod], "comma",
#              lazy.prev_screen(),
#              desc='Move focus to prev monitor'
#              ),
#          ### Treetab controls
#           Key([mod, "shift"], "h",
#              lazy.layout.move_left(),
#              desc='Move up a section in treetab'
#              ),
#          Key([mod, "shift"], "l",
#              lazy.layout.move_right(),
#              desc='Move down a section in treetab'
#              ),
#          ### Window controls
#          Key([mod], "j",
#              lazy.layout.down(),
#              desc='Move focus down in current stack pane'
#              ),
#          Key([mod], "k",
#              lazy.layout.up(),
#              desc='Move focus up in current stack pane'
#              ),
#          Key([mod, "shift"], "j",
#              lazy.layout.shuffle_down(),
#              lazy.layout.section_down(),
#              desc='Move windows down in current stack'
#              ),
#          Key([mod, "shift"], "k",
#              lazy.layout.shuffle_up(),
#              lazy.layout.section_up(),
#              desc='Move windows up in current stack'
#              ),
#          Key([mod], "h",
#              lazy.layout.shrink(),
#              lazy.layout.decrease_nmaster(),
#              desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
#              ),
#          Key([mod], "l",
#              lazy.layout.grow(),
#              lazy.layout.increase_nmaster(),
#              desc='Expand window (MonadTall), increase number in master pane (Tile)'
#              ),
#          Key([mod], "n",
#              lazy.layout.normalize(),
#              desc='normalize window size ratios'
#              ),
#          Key([mod], "m",
#              lazy.layout.maximize(),
#              desc='toggle window between minimum and maximum sizes'
#              ),
#          Key([mod, "shift"], "f",
#              lazy.window.toggle_floating(),
#              desc='toggle floating'
#              ),
#          Key([mod], "f",
#              lazy.window.toggle_fullscreen(),
#              desc='toggle fullscreen'
#              ),
#          ### Stack controls
#          Key([mod, "shift"], "Tab",
#              lazy.layout.rotate(),
#              lazy.layout.flip(),
#              desc='Switch which side main pane occupies (XmonadTall)'
#              ),
#           Key([mod], "space",
#              lazy.layout.next(),
#              desc='Switch window focus to other pane(s) of stack'
#              ),
#          Key([mod, "shift"], "space",
#              lazy.layout.toggle_split(),
#              desc='Toggle between split and unsplit sides of stack'
#              ),
#          # Emacs programs launched using the key chord CTRL+e followed by 'key'
#         # #  KeyChord([mod],"e", [
#         # #      Key([], "e",
#         # #          lazy.spawn("emacsclient -c -a 'emacs'"),
#         # #          desc='Emacsclient Dashboard'
#         # #          ),
#         # #      Key([], "a",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(emms)' --eval '(emms-play-directory-tree \"~/Music/\")'"),
#         # #          desc='Emacsclient EMMS (music)'
#         # #          ),
#         # #      Key([], "b",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(ibuffer)'"),
#         # #          desc='Emacsclient Ibuffer'
#         # #          ),
#         # #      Key([], "d",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(dired nil)'"),
#         # #          desc='Emacsclient Dired'
#         # #          ),
#         # #      Key([], "i",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(erc)'"),
#         # #          desc='Emacsclient ERC (IRC)'
#         # #          ),
#         # #      Key([], "n",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(elfeed)'"),
#         # #          desc='Emacsclient Elfeed (RSS)'
#         # #          ),
#         # #      Key([], "s",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(eshell)'"),
#         # #          desc='Emacsclient Eshell'
#         # #          ),
#         # #      Key([], "v",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(+vterm/here nil)'"),
#         # #          desc='Emacsclient Vterm'
#         # #          ),
#         # #      Key([], "w",
#         # #          lazy.spawn("emacsclient -c -a 'emacs' --eval '(doom/window-maximize-buffer(eww \"distro.tube\"))'"),
#         # #          desc='Emacsclient EWW Browser'
#         # #          )
#         #  ]),
#          # Dmenu scripts launched using the key chord SUPER+p followed by 'key'
#          KeyChord([mod], "p", [
#              Key([], "h",
#                  lazy.spawn("dm-hub"),
#                  desc='List all dmscripts'
#                  ),
#              Key([], "a",
#                  lazy.spawn("dm-sounds"),
#                  desc='Choose ambient sound'
#                  ),
#              Key([], "b",
#                  lazy.spawn("dm-setbg"),
#                  desc='Set background'
#                  ),
#              Key([], "c",
#                  lazy.spawn("dtos-colorscheme"),
#                  desc='Choose color scheme'
#                  ),
#              Key([], "e",
#                  lazy.spawn("dm-confedit"),
#                  desc='Choose a config file to edit'
#                  ),
#              Key([], "i",
#                  lazy.spawn("dm-maim"),
#                  desc='Take a screenshot'
#                  ),
#              Key([], "k",
#                  lazy.spawn("dm-kill"),
#                  desc='Kill processes '
#                  ),
#              Key([], "m",
#                  lazy.spawn("dm-man"),
#                  desc='View manpages'
#                  ),
#              Key([], "n",
#                  lazy.spawn("dm-note"),
#                  desc='Store and copy notes'
#                  ),
#              Key([], "o",
#                  lazy.spawn("dm-bookman"),
#                  desc='Browser bookmarks'
#                  ),
#              Key([], "p",
#                  lazy.spawn("passmenu -p \"Pass: \""),
#                  desc='Logout menu'
#                  ),
#              Key([], "q",
#                  lazy.spawn("dm-logout"),
#                  desc='Logout menu'
#                  ),
#              Key([], "r",
#                  lazy.spawn("dm-radio"),
#                  desc='Listen to online radio'
#                  ),
#              Key([], "s",
#                  lazy.spawn("dm-websearch"),
#                  desc='Search various engines'
#                  ),
#              Key([], "t",
#                  lazy.spawn("dm-translate"),
#                  desc='Translate text'
#                  )
#          ])
# ]

groups = [Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='bsp'),
          Group("", layout='monadtall'),
          Group("", layout='floating')]


# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder(mod)


# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('terminal', terminal, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('text_editor', text_editor, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('file_manager2', file_manager2, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
    DropDown('process_viewer', process_viewer, width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('terminal')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('text_editor')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('file_manager2')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('process_viewer')),
])  

layouts = [
    layout.MonadTall(border_focus = colors[0], border_normal = colors[0], border_width = 1, margin = 8),
    #layout.Bsp(border_focus = colors[4], margin = 5),
    #layout.RatioTile(border_focus = colors[4], margin = 2),
    #layout.TreeTab(border_focus = colors[4], margin = 2),
    #layout.Tile(border_focus = colors[4], margin = 2),
    #layout.Stack(num_stacks=2),
    #layout.Bsp(),
    #layout.Matrix(),
    #layout.MonadWide(),
    #layout.TreeTab(),
    #layout.VerticalTile(),
    #layout.Zoomy(),
]

# layout_theme = {"border_width": 2,
#                 "margin": 8,
#                 "border_focus": '6082A9',
#                 "border_normal": "000000"
#                 }

# layouts = [
#     #layout.MonadWide(**layout_theme),
#     #layout.Bsp(**layout_theme),
#     layout.Stack(stacks=2, **layout_theme),
#     #layout.Columns(**layout_theme),
#     #layout.RatioTile(**layout_theme),
#     #layout.Tile(shift_windows=True, **layout_theme),
#     #layout.VerticalTile(**layout_theme),
#     #layout.Matrix(**layout_theme),
#     #layout.Zoomy(**layout_theme),
#     layout.MonadTall(**layout_theme),
#     layout.Max(**layout_theme),
#     # layout.Stack(num_stacks=2),
#     layout.RatioTile(**layout_theme),
#     layout.TreeTab(
#          font = "Ubuntu",
#          fontsize = 10,
#          sections = ["FIRST", "SECOND", "THIRD", "FOURTH"],
#          section_fontsize = 10,
#          border_width = 2,
#          bg_color = "1c1f24",
#          active_bg = "6082A9",
#          active_fg = "000000",
#          inactive_bg = "a9a1e1",
#          inactive_fg = "1c1f24",
#          padding_left = 0,
#          padding_x = 0,
#          padding_y = 5,
#          section_top = 10,
#          section_bottom = 20,
#          level_shift = 8,
#          vspace = 3,
#          panel_width = 200
#          ),
#     layout.Floating(**layout_theme)
# ]
prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widget_defaults = dict(
    font = 'Hack',
    fontsize = 14,
    padding = 2,
    background = colors[0]
)
extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widgets_list = [
                    widget.Image(
                        filename = '~/.config/qtile/icons/python.png',
                        scale = 'False',
                        margin_x = 8,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(file_launcher2)}
                        ),
                    widget.GroupBox(
                        padding = 4,
                        active = colors[2],
                        inactive = colors[1],
                        highlight_color = [backgroundColor, workspaceColor],
                        highlight_method = 'line',
                        ),
                widget.Prompt(),
                    widget.TextBox(
                        text='\u25e2',
                        padding = 0,
                        fontsize = 50,
                        background = backgroundColor,
                        foreground = workspaceColor),
                widget.CurrentLayout(
                        scale = 0.7,
                        background = workspaceColor
                        ),
                    widget.TextBox(
                        text='\u25e2',
                        padding = 0,
                        fontsize = 50,
                        background = workspaceColor,
                    foreground = backgroundColor
                        ),
                widget.WindowName(
                        foreground = colors[5],
                        ),
                    widget.Chord(
                        chords_colors = {
                            'launch': (foregroundColor, foregroundColor),
                        },
                        name_transform=lambda name: name.upper(),
                        ),
                    widget.TextBox(
                        text='\u25e2',
                        padding = 0,
                        fontsize = 50,
                        background = backgroundColor,
                        foreground = foregroundColorTwo
                        ),
                    widget.TextBox(
                        text='\u25e2',
                        padding = 0,
                        fontsize = 14,
                        background = foregroundColorTwo,
                        foreground = foregroundColorTwo
                        ),
                    widget.Net(
                        interface = "wlp4s0",
                        format = ' {down} ↓↑ {up}',
                        foreground = colors[7],
                        background = foregroundColorTwo,
                        padding = 8
                        ),
                    widget.CPU(
                        format = '  {freq_current}GHz {load_percent}%',
                        background = foregroundColorTwo,
                        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
                        foreground = colors[10],
                        padding = 8
                        ),
                    widget.Memory(
                        background = foregroundColorTwo,
                        foreground = colors[4],
                        fmt = '  {}',
                        padding = 8
                        ),
                    widget.CheckUpdates(
                        update_interval = 3600,
                        distro = "Manjaro",
                        display_format = "Updates: {updates} ",
                        no_update_string = " No Updates",
                        colour_have_updates = colors[9],
                        colour_no_updates = colors[5],
                        padding = 8,
                        background = foregroundColorTwo
                        ),
                    widget.Volume(
                        foreground = colors[8],
                        background = foregroundColorTwo,
                        fmt = ': {}',
                        padding = 8
                        ),

                    # widget.Battery(
                    #     charge_char ='',
                    #     discharge_char = '',
                    #     format = '  {percent:2.0%} {char}',
                    #     foreground = colors[6],
                    #     background = foregroundColorTwo,
                    #     padding = 8,
                    #     ),
                    widget.TextBox(
                        text='\u25e2',
                        padding = 0,
                        fontsize = 50,
                        background = foregroundColorTwo,
                        foreground = backgroundColor
                        ),
                    widget.Systray(
                        padding = 8
                        ),
                    widget.Clock(format=' %a, %d. %m. %Y. |  %I:%M %p',
                        foreground = colors[2],
                        background = backgroundColor,
                        padding = 8
                        ),
                    widget.QuickExit(
                        fmt = ' ',
                        foreground = colors[9],
                        padding = 8
                        ),              
                ]

    return widgets_list
# def init_widgets_screen1():
#     widgets_screen1 = init_widgets_list()
#     # del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
#     return widgets_screen1

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    # del widgets_screen1[9:10]               # Slicing removes unwanted widgets (systray) on Monitors 1,3
    return widgets_screen1

# def init_widgets_screen2():
#     widgets_screen2 = init_widgets_list()
#     return widgets_screen2                 # Monitor 2 will display all widgets in widgets_list

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]
            # Screen(top=bar.Bar(widgets=init_widgets_screen2(), opacity=1.0, size=20)),
            # Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=1.0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    # widgets_screen2 = init_widgets_screen2()

def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)

def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)

def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)

def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)

def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start = lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start = lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

#dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(border_focus = colors[4], float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class = 'gimp'),  # gitk
    Match(wm_class = 'mypaint'),  # gitk
    Match(wm_class = 'ssh-askpass'),  # ssh-askpass
    Match(title = 'branchdialog'),  # gitk
    Match(title = 'pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# Programms to start on log inTTYTEEEPP5777654
@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# : Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
