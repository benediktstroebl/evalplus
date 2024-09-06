from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_levels = []
    current_level = 0
    for group in paren_string.split():
        if len(group) == 1:
            current_level += 1
        elif current_level > 0 and group[0] == '(':
            current_level -= 1
        else:
            current_level = len(group)
    return [max_levels[i] for i in range(len(max_levels))]
