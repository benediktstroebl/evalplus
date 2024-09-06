from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    num_parens = 0
    level = 0
    levels = []
    for char in paren_string:
        if char == '(':
            num_parens += 1
            if level == 0:
                level = num_parens
        elif char == ')':
            num_parens -= 1
        if num_parens == 0:
            levels.append(level)
            level = 0
    levels.append(level)
    return
