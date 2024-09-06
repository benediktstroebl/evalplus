from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = {}
    level = []

    for char in paren_string:
        if char == '(':
            level.append(1)
        elif char == ')':
            level.pop()
            count[len(level)] = 1
        else:
            count[len(level)] += 1

    return count.values()

