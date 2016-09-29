#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module provides a function that knows what you mean"""


def know_what_i_mean(wink, numwink=2):
    """Does some multiplication, get rid off white space and return a string

    Args:
        wink (mixed): Arg to be multiplied with numwik
        numwik (int): Arg to multiply wink

    Returns:
        str: New argument concatenated with original arguments and comma

    Examples:
        >>> know_what_i_mean('wink ')
        'Know what I mean? wink wink, nudge nudge'
    """
    winks = (wink * numwink).strip()
    nudges = ('nudge ' * numwink).strip()
    retstr = 'Know what I mean? {}, {}'.format(winks, nudges)
    return retstr
