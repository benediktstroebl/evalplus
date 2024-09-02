from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_string ='' + paren_string +''

    num_groups = len(paren_string.split(' '))
    nested_parens = [0] * num_groups
    for group in range(num_groups):
        opening, closing = paren_string[group].count('('), paren_string[group].count(')')
        nested_parens[group] = max(opening, closing)

    return nested_paren
