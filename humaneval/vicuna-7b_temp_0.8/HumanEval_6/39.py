from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = [0] * len(paren_string)

    for i, c in enumerate(paren_string):
        if c == '(':
            levels[i] = levels[i] + 1
        elif c == ')':
            levels[i] = levels[i] - 1
        elif c == '':
            pass
        else:
            return [max(lvl for lvl in levels) for _ in paren_string]

    return levels

