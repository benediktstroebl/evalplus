from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for i in paren_string:
        for j in i:
            if j == '(':
                result.append(0)
            elif j == ')':
                result[-1] += 1
            elif j == ':':
                result[-1] += 2
            elif j == ' ':
                pass
    return result

