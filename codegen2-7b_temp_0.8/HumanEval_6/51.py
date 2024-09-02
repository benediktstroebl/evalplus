from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens = [1]
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            parens[-1] += 1
            parens.append(1)
        else:
            parens[-1] -= 1
            if parens[-1] == 0:
                parens.pop()
        i += 1
    return parens

