# -*- coding: utf-8 -*-

# Curlew - Easy to use multimedia converter
#
# Copyright (C) 2012-2017 Fayssal Chamekh <chamfay@gmail.com>
#
# Released under terms on waqf public license.
#
# Curlew is free software; you can redistribute it and/or modify it 
# under the terms of the latest version waqf public license as published by 
# ojuba.org.
#
# Curlew is distributed in the hope that it will be useful, but WITHOUT 
# ANY WARRANTY; without even the implied warranty 
# of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#        
# The latest version of the license can be found on:
# http://waqf.ojuba.org/license

from shutil import which
from modules.configs import set_s_config

PLAYERS_LIST = [
    'mpv',
    'avplay',
    'ffplay',
    'mplayer',
    'smplayer',
    'vlc',
    'totem',
    'kplayer',
    'kmplayer',
    'parole'
    ]

def choose_player():
    for player in PLAYERS_LIST:
        if which(player):
            set_s_config('player', player)
            return player
    return None


