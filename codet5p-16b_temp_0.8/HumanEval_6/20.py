from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_depth = 0
    result = []

    for depth, char in enumerate(paren_string):
        if char == '(':
            result.append(depth)
            max_depth = max(max_depth, depth)
        elif char == ')':
            result.append(depth)

    return result[max_depth:]

