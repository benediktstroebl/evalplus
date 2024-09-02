from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # char count and stack
    char_count = 0
    depth = 0

    # iterate each paren
    for char in paren_string:
        if char == "(":
            char_count += 1
            depth += 1
        elif char == ")":
            char_count -= 1
            if char_count == 0:
                depth -= 1

    return [depth, char_count]

