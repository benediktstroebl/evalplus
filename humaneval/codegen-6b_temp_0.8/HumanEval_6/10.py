from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # split by spaces
    paren_list = paren_string.split(' ')

    nested_parens = []

    max_nested_level = 0
    for paren in paren_list:
        nested_parens.append(find_nested_level(paren))
        max_nested_level = max(max_nested_level, nested_parens[-1])

    return nested_parens

