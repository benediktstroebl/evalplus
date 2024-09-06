from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    open_parens = 0
    max_levels = []

    for char in paren_string:
        if char == "(":
            open_parens += 1
        elif char == ")":
            max_levels.append(open_parens)
            open_parens -= 1

    return max_levels
