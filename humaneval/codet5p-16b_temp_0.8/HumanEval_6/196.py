from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.split()
    list_of_nested_parens = []

    for i in paren_string:
        if i == '(':
            list_of_nested_parens.append(1)
        elif i == ')':
            list_of_nested_parens.append(-1)
        else:
            list_of_nested_parens.append(0)

    return [list_of_nested_parens.count(i) for i in range(-1, 3)]

