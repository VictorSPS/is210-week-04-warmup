#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Defining a function with three parameters"""

def too_many_kittens(kittens, litterboxes, catfood):
    """Does some comparison and return a boolean value as a result of it

    Args:
      kittens(int): Arg to be compared with litterboxes
      litterboxes(int): Arg to be compared with kittens
      catfood(bool): Arg representing whether or not any catfood exists

    Returns:
       boolean: value of the comparison statement

    Examples:
       >>>too_many_kittens(13, 12, True)
       True
    """
    if not (litterboxes >= kittens and catfood):
        return True
    else:
        return False
