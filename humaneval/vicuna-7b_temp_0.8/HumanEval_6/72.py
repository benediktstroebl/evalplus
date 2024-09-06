from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = [0] * 2  # Initialize an array to store the maximum nesting of parentheses.
    for char in paren_string:
        if char == '(':
            nested_parens[0] += 1
        elif char == ')':
            nested_parens[1] += 1
        else:
            break
    return nested_parens

