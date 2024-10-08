from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    curr_level = 0
    max_level = 0
    parens_levels = []

    for i, char in enumerate(paren_string):
        if char == '(':
            curr_level += 1
        elif char == ')':
            curr_level -= 1

        if curr_level > max_level:
            max_level = curr_level
            parens_levels.append(max_level)

        if curr_level == 0 and max_level > 0:
            max_level = 0
            parens_levels.append(0)

    return parens_levels

