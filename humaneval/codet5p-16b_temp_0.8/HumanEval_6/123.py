from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split(' ')
    res = []
    for paren in parens:
        level = 0
        for c in paren:
            if c == '(':
                level += 1
            elif c == ')':
                level -= 1
            if level == -1:
                break
        if level == -1:
            res.append(0)
        else:
            res.append(level)
    return res

