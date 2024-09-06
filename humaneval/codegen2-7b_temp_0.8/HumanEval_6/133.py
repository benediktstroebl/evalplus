from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level = 1
    nested = 0
    for char in paren_string:
        if char == "(":
            nested += 1
        elif char == ")":
            nested -= 1
            if nested == -1:
                level += 1
    return [level, nested
