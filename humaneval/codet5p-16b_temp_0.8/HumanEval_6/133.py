from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens: List[int] = []

    for item in paren_string.split(' '):
        if item[0] == '(' and item[-1] == ')':
            nested_parens.append(parse_nested_parens_helper(item[1:-1]))

    return nested_parens

