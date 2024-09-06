from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    groups = paren_string.split()

    max_depth = 0
    depth = 0
    for g in groups:
        curr_depth = g.count('(') - g.count(')')
        if curr_depth > depth:
            depth = curr_depth
            max_depth = curr_depth

    return [max_depth]

