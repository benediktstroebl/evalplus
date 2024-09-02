from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level, _, res = 0, 0, []
    for i in paren_string:
        if i == '(':
            level += 1
        elif i == ')':
            level -= 1
        if level == 0:
            res.append(i)
    return res

