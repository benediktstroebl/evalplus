from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    max_depth_groups = []
    depth = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif char == ')':
            depth -= 1
            if depth == max_depth:
                max_depth_groups.append(i)
    return [max_depth - i for i in reversed(max_depth_groups)]

