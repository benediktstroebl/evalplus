from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Base case: if no parens in string, return empty list
    if not paren_string:
        return []

    # Store all groups in a list
    groups = paren_string.split()

    # Store each group of parens and its max depth of nesting
    depths = []
    for group in groups:
        # Find max depth of nesting
        depths.append(max_nesting_depth(group))
    return depths

