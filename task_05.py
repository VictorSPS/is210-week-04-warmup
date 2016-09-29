#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Default value in our function definition"""

def defaults(my_required, my_optional=True):
    """Set a default value and return logical comparison

    Args:
       my_required(mixed): Arg compared with my_optional
       my_optional(bool): Arg default, compared with my_required

    Returns:
       bool: result of logical comparison

    Examples:
       >>>defaults(True, False)
       False
    """
    return my_optional is my_required
