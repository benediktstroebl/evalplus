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

    open_paren_count = 0
    closed_paren_count = 0

    if paren_string[0] == '(':
        open_paren_count += 1
        closed_paren_count += 1

    deepest_level = 0
    max_level = 0

    for c in paren_string:
        if c == '(':
            open_paren_count += 1
            closed_paren_count = 0
            deepest_level = max(deepest_level, open_paren_count)
        elif c == ')':
            open_paren_count -= 1
            closed_paren_count += 1
            max_level = max(max_level, open_paren_count - closed_paren_count)

    return [deepest_level, max_level]

