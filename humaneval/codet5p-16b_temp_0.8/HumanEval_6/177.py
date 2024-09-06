from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = []
    start = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            parens.append(start)
            start = i
        elif paren_string[i] == ')':
            parens.append(i)
    parens.append(len(paren_string))

    deepest_level = []
    for i in range(1, len(parens) - 1):
        depth = parens[i] - parens[i - 1] - 1
        deepest_level.append(depth)

    return deepest_level

