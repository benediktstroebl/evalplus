from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_levels = []
    prev_level = 0
    for paren in paren_string.split(' '):
        level = paren.count('(') - paren.count(')')
        paren_levels.append(level - prev_level)
        prev_level = level
    return paren_levels
    

