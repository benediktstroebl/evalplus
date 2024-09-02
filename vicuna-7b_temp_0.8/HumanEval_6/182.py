from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    num_parens = 0
    paren_levels = [0] * len(paren_string)
    for char in paren_string:
        if char == '(':
            num_parens += 1
            paren_levels[num_parens - 1] += 1
        elif char == ')':
            num_parens -= 1
            paren_levels[num_parens] -= 1
            if num_parens > 0:
                paren_levels[num_parens - 1] += 1
    return paren_levels

