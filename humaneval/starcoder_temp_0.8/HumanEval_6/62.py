from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens: List[str] = paren_string.split(' ')
    parens_count: List[int] = []

    for paren in parens:
        open_paren = paren.count('(')
        close_paren = paren.count(')')
        parens_count.append(max(open_paren, close_paren))
    return parens_count

