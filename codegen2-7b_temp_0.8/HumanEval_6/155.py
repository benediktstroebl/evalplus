from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for i in range(len(paren_string)):
        c = paren_string[i]
        if c == '(':
            nested_parens.append(1)
        elif c == ')':
            nested_parens[-1] -= 1
            if nested_parens[-1] == 0:
                nested_parens.pop()
    return nested_parens[::-1
