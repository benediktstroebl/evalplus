from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_levels = 0
    result = []

    for group in paren_string.split():
        if group == '(':
            max_levels += 1
        elif group == ')':
            result.append(max_levels)
            max_levels -= 1

    result.append(max_levels)
    return result

