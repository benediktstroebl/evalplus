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

    paren_count = 0
    max_count = 0
    max_idx = 0
    for idx, char in enumerate(paren_string):
        if char == '(':
            paren_count += 1
        elif char == ')':
            paren_count -= 1
        if paren_count > max_count:
            max_count = paren_count
            max_idx = idx + 1
    return [max_count, max_idx]

