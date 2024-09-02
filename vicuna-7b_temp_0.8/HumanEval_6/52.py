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
    for char in paren_string:
        if char == '(':
            max_depth = max(max_depth, 1)
        elif char == ')':
            max_depth = max(max_depth, 0)
        elif char == ' ':
            pass
        elif char == ']':
            result.append(max_depth)
            max_depth = 0
    result.append(max_depth)
    return result

