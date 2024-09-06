from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_levels = [0] * 5
    for char in paren_string:
        if char == '(':
            nesting_levels[0] += 1
        elif char == ')':
            nesting_levels[0] -= 1
        else:
            nesting_levels[1:5] = [nesting_levels[1:5][0] + 1, 
                                   nesting_levels[1:5][1] + 1,
                                   nesting_levels[1:5][2] + 1]
                                   if char == '(' else [0] * 3
    return nesting_levels

