from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens = [0]
    for i in paren_string:
        if i == '(':
            parens[-1] = max(parens[-1], parens[-2] + 1)
        elif i == ')':
            parens[-1] = max(parens[-1], parens[-1] - 1)
    return parens

