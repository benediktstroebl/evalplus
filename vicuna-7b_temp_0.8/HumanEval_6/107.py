from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level_count = [0] * 5

    for opening, closing in zip(paren_string.opening_pairs, paren_string.closing_pairs):
        if opening == '(' and closing == ')':
            level_count[0] += 1
        elif opening == '[' and closing == ']':
            level_count[1] += 1
        elif opening == '{' and closing == '}':
            level_count[2] += 1
        elif opening == '`' and closing == '`':
            level_count[3] += 1
        elif opening == '(' and closing == ')':
            level_count[4] += 1

    return level_count

