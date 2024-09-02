from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    max_levels = []
    current_max = 0

    for char in paren_string:
        if char == '(':
            current_max += 1
        if char == ')':
            current_max -= 1
        if current_max > len(max_levels):
            max_levels.append(current_max)
        elif current_max == len(max_levels):
            max_levels.append(current_max)

    return max_levels

