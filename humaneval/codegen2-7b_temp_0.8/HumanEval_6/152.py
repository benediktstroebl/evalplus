from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested = 0
    current_level = 0
    max_nested = 0
    result = []
    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
            nested = max(nested, current_level)
        if current_level > max_nested:
            max_nested = current_level
    result.append(max_nested)
    return
