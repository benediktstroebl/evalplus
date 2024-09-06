from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_string = paren_string.replace(' ', '')
    if len(paren_string) == 0:
        return []
    max_level = 0
    depth = 0
    current_max = 0
    for char in paren_string:
        if char == '(':
            depth += 1
            current_max = max(current_max, depth)
            max_level = max(max_level, current_max)
        if char == ')':
            depth -= 1
            current_max = max(current_max, depth)
            max_level = max(max_level, current_max)
    return [max_level]

