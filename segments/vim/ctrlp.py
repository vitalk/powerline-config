#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8:noet
from __future__ import (unicode_literals, division, absolute_import, print_function)
import os
try:
    import vim
except ImportError:
    vim = object()

from powerline.bindings.vim import getbufvar
from powerline.segments.vim import window_cached


@window_cached
def ctrlp(pl, side):
    '''

    Highlight groups used: ``ctrlp:regex`` or ``background``, ``ctrlp:prev`` or ``background``, ``ctrlp:item`` or ``file_name``, ``ctrlp:next`` or ``background``, ``ctrlp:marked`` or ``background``, ``ctrlp:focus`` or ``background``, ``ctrlp:byfname`` or ``background``, ``ctrlp:progress`` or ``file_name``, ``ctrlp:progress`` or ``file_name``.
    '''
    ctrlp_type = getbufvar('%', 'powerline_ctrlp_type')
    ctrlp_args = getbufvar('%', 'powerline_ctrlp_args')

    return globals()['ctrlp_stl_{0}_{1}'.format(side, ctrlp_type)](pl, *ctrlp_args)


def ctrlp_stl_left_main(pl, focus, byfname, regex, prev, item, next, marked):
    '''

    Highlight groups used: ``ctrlp:regex`` or ``background``, ``ctrlp:prev`` or ``background``, ``ctrlp:item`` or ``file_name``, ``ctrlp:next`` or ``background``, ``ctrlp:marked`` or ``background``.
    '''
    marked = marked[2:-1]
    segments = []

    if int(regex):
        segments.append({
            'contents': 'regex',
            'highlight_groups': ['ctrlp:regex', 'background'],
        })

    segments += [
        {
            'contents': prev + ' ',
            'highlight_groups': ['ctrlp:prev', 'background'],
            'draw_inner_divider': True,
            'priority': 40,
        },
        {
            'contents': item,
            'highlight_groups': ['ctrlp:item', 'file_name'],
            'draw_inner_divider': True,
            'width': 10,
            'align': 'c',
        },
        {
            'contents': ' ' + next,
            'highlight_groups': ['ctrlp:next', 'background'],
            'draw_inner_divider': True,
            'priority': 40,
        },
    ]

    if marked != '-':
        segments.append({
            'contents': marked,
            'highlight_groups': ['ctrlp:marked', 'background'],
            'draw_inner_divider': True,
        })

    return segments


def ctrlp_stl_right_main(pl, focus, byfname, regex, prev, item, next, marked):
    '''

    Highlight groups used: ``ctrlp:focus`` or ``background``, ``ctrlp:byfname`` or ``background``.
    '''
    segments = [
        {
            'contents': focus,
            'highlight_groups': ['ctrlp:focus', 'background'],
            'draw_inner_divider': True,
            'priority': 50,
        },
        {
            'contents': byfname,
            'highlight_groups': ['ctrlp:byfname', 'background'],
            'priority': 50,
        },
    ]

    return segments


def ctrlp_stl_left_prog(pl, progress):
    '''

    Highlight groups used: ``ctrlp:progress`` or ``file_name``.
    '''
    return [
        {
            'contents': 'Loading...',
            'highlight_groups': ['ctrlp:progress', 'file_name'],
        },
    ]


def ctrlp_stl_right_prog(pl, progress):
    '''

    Highlight groups used: ``ctrlp:progress`` or ``file_name``.
    '''
    return [
        {
            'contents': str(progress),
            'highlight_groups': ['ctrlp:progress', 'file_name'],
        },
    ]
