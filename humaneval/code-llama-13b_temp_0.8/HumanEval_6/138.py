from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    result = []
    for paren_group in paren_string.split():
        if not paren_group:
            continue
        # Tracks the current level of nesting.
        level = 0
        # The max level encountered so far.
        max_level = 0
        for character in paren_group:
            if character == '(':
                level += 1
                max_level = max(level, max_level)
            if character == ')':
                level = level - 1
        result.append(max_level)
    return result

