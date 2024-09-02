from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nest_levels = []

    open_brackets = 0

    for i, c in enumerate(paren_string):
        if c == '(':
            open_brackets += 1
        elif c == ')':
            open_brackets -= 1
            if open_brackets == 0:
                nest_levels.append(i + 1)

    return nest_levels
