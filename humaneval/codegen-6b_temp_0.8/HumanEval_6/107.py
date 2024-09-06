from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    start_idx = 0
    while start_idx < len(paren_string):
        end_idx = get_closing_paren(paren_string, start_idx)
        nested_parens.append(end_idx - start_idx + 1)
        start_idx = end_idx + 1
    return nested_parens

