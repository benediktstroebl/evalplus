from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    deepest_level = 0
    levels = []
    for group in paren_string.split(' '):
        n = 0
        for c in group:
            if c == '(':
                n += 1
            elif c == ')':
                n -= 1
                if n < deepest_level:
                    deepest_level = n
            else:
                raise ValueError(f"Unexpected character {c} in {group}")
        levels.append(deepest_level)
        deepest_level = 0

    return levels

