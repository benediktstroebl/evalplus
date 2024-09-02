from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = []
    paren_string = paren_string.replace('()', '0')
    for paren in paren_string.split():
        if paren == '0':
            levels.append(0)
        else:
            level = len(paren)
            levels.append(level)
    return levels

