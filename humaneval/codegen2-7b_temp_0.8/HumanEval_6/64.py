from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens_levels = []
    for paren_string in paren_string.split():
        paren_level = 0
        for char in paren_string:
            if char == '(':
                paren_level += 1
            elif char == ')':
                paren_level -= 1
            if paren_level == -1:
                break
        nested_parens_levels.append(paren_level)
    return nested_parens_levels

