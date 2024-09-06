from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting = [0] * 2
    for opening, closing in ((True, True), (False, False)):
        for i, char in enumerate(paren_string):
            if char == '(' and nesting[0] == 0:
                nesting[0] = i
            elif char == ')' and nesting[0] != 0:
                nesting[0] = nesting[0] - 1
    return nesting

