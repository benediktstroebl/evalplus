from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split()

    result = []

    for paren in parens:
        open_parens = 0
        close_parens = 0
        for c in paren:
            if c == '(':
                open_parens += 1
            elif c == ')':
                close_parens += 1
        result.append(max(open_parens, close_parens))

    return result
