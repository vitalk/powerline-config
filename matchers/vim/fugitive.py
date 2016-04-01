#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import os
try:
    import vim
except ImportError:
    vim = {}  # NOQA

from powerline.bindings.vim import vim_getbufoption


def commit(matcher_info):
    return vim_getbufoption(matcher_info, 'filetype') == 'gitcommit'


def fugitive(matcher_info):
    name = matcher_info['buffer'].name
    return name and name.find('fugitive://') == 0
