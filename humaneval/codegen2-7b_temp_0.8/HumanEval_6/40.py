from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_levels = []

    for level, paren_string in enumerate(paren_string.split()):
        paren_string = '(' + paren_string + ')'

        if '(' not in paren_string:
            nesting_levels.append(level + 1)
        else:
            nesting_levels.append(max(nesting_levels) + 1)

    return nesting_levels

