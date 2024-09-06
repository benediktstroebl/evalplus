from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parenthesis_list = [s for s in paren_string.split() if s == '(' or s == ')']
    result = []
    for s in parenthesis_list:
        if s == '(':
            result.append(1)
        elif s == ')':
            result[-1] -= 1
            if result[-1] == 0:
                result.pop()
    return result

