from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nesting = []
    for character in paren_string:
        if character == '(':
            nesting.append(1)
        elif character == ')':
            nesting.append(0)
        elif character == ' ':
            nesting[-1] += 1
            nesting.append(0)
    return nesting

