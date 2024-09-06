from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths = [0] * (len(paren_string) + 1)
    for i in range(1, len(paren_string) + 1):
        if paren_string[i - 1] == '(':
            depths[i] = depths[i - 1] + 1
        elif paren_string[i - 1] == ')':
            depths[i] = depths[i - 1] - 1
        # we have to look at the max because the first depth is always 0
        depths[i] = max(0, depths[i])
    return depths

