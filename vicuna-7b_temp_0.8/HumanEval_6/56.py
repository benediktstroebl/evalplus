from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for opening_paren in paren_string.split():
        nesting = 0
        for char in opening_paren:
            if char == '(':
                nesting += 1
            elif char == ')':
                nesting -= 1
            else:
                break
        nested_parens.append(nesting)
    return nested_parens

