from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_count = [0] * 4
    level_max = 0
    for opening, closing in zip(paren_string.opening_pairs, paren_string.closing_pairs):
        for i in range(len(opening)):
            if opening[i] == '(':
                nested_count[level_max] += 1
                level_max += 1
        for i in range(len(closing)):
            if closing[i] == ')':
                nested_count[level_max] -= 1
                level_max -= 1
    return nested_count[:level_max]
