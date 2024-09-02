from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split(' ')
    level_of_nesting = [0] * len(parens)
    max_level_of_nesting = [0] * len(parens)
    for i, paren in enumerate(parens):
        open_paren = 0
        close_paren = 0
        for j, c in enumerate(paren):
            if c == '(':
                open_paren += 1
            else:
                close_paren += 1
            if open_paren == close_paren:
                level_of_nesting[i] = open_paren
                max_level_of_nesting[i] = j + 1
                break
    return max_level_of_nesting

