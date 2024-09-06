from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if not paren_string:
        return []

    def _parse_paren_level(s: str):
        level = 0
        for c in s:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
                if level < 0:
                    return level
        return level

    paren_levels = []
    for parens in paren_string.split():
        level = _parse_paren_level(parens)
        paren_levels.append(level)

    return paren_levels

