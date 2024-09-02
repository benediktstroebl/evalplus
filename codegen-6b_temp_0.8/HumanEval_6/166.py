from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    is_opening = False
    depth = 0
    max_depth = 0

    for paren in paren_string:
        if paren == '(':
            is_opening = True
            depth += 1
            max_depth = max(max_depth, depth)
        elif paren == ')':
            is_opening = False
            depth -= 1

    result = []
    current_depth = max_depth
    for depth_value in range(max_depth, -1, -1):
        result.append(current_depth - depth_value)

    return result

