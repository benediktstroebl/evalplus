from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = []
    max_level = 0
    for group in paren_string.split():
        level = 0
        for c in group:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
        if level > max_level:
            max_level = level
        groups.append(level)

    return groups

