from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    start = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            nested_parens.append(i)
        elif char == ')':
            if len(nested_parens) == 0:
                raise Exception('Unexpected end of string')
            nested_parens.pop()
    return nested_parens

