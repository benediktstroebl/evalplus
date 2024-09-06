from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = set()
    for open_paren in paren_string.strip(' ').split('('):
        for close_paren in paren_string.strip(' ').split(')'):
            if open_paren == close_paren:
                nested_parens.add(1)
            else:
                nested_parens.add(0)
    return [len(nested_parens) - 1 - i for i in range(len(nested_parens))]