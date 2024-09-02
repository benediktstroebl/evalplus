from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_string = paren_string.replace(' ', '')
    result = 0
    max_level = 0
    for c in paren_string:
        if c == '(':
            max_level += 1
        elif c == ')':
            max_level -= 1
        result = max(result, max_level)
    return result + 1


import pytest

