from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = set()
    current_nesting = 0
    for opening_paren in paren_string:
        if not opening_paren:
            nested_parens.add(0)
        else:
            current_nesting += 1
            nested_parens.add(current_nesting)
    return [nested_parens.count(n) for n in nested_parens]