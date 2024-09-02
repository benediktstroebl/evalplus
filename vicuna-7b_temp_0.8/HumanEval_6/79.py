from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = [0] * 4
    deepest = 0

    for char in paren_string:
        if char == '(':
            count[0] += 1
        elif char == ')':
            count[-1] -= 1
            if count[-1] < 0:
                deepest += 1
                count[-1] = 0

    return deepest

