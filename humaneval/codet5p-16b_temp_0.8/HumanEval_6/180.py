from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.split()
    nested_parens = []
    nested_parens_level = []

    for paren in paren_string:
        if paren.count('(') == paren.count(')'):
            nested_parens.append(paren)
        elif paren.count('(') == paren.count(')'):
            if paren[1] == '(':
                nested_parens_level.append(paren)
            else:
                nested_parens_level.pop()

    return nested_parens_level
