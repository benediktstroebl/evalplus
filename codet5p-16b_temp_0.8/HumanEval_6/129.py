from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    res = []

    cur_level = 0
    max_level = 0
    for c in paren_string:
        if c == '(':
            cur_level += 1
            max_level = max(max_level, cur_level)
        elif c == ')':
            cur_level -= 1
        else:
            pass
        res.append(cur_level)
    return res
