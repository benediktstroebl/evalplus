from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth_of_parens = []

    for nested_parens in paren_string.split():
        depth = 0
        for paren in nested_parens:
            depth += 1 if paren == '(' else -1
        depth_of_parens.append(depth)

    return depth_of_parens

