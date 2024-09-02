from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_depth = 0
    current_depth = 0

    depth_tracker = []
    for c in paren_string:
        if c == '(':
            depth_tracker.append(current_depth)
            current_depth += 1

        if c == ')':
            if len(depth_tracker) > 0:
                max_depth = max(max_depth, current_depth)
                current_depth = depth_tracker.pop()
            else:
                current_depth = 0

    return [max_depth] * len(paren_string.split(' '))

