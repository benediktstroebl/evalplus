from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_levels = []
    for char in paren_string:
        if char == '(':
            paren_levels.append(0)
        elif char == ')':
            paren_levels[-1] += 1
            if paren_levels[-2] == 0:
                paren_levels.pop()
    return paren_levels

