from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    group_open = 0
    levels = []
    for char in paren_string:
        if char == '(':
            group_open += 1
        elif char == ')':
            group_open -= 1
        if group_open == 0:
            levels.append(0)
        else:
            levels[-1] += 1

    return levels

