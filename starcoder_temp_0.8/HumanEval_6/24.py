from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    current_level = 0
    nested_levels = []
    for char in paren_string:
        if char == '(':
            current_level += 1
        else:
            current_level -= 1
        nested_levels.append(current_level)
    return nested_levels

