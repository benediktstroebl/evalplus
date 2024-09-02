from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    nested_parens = []

    for i in paren_string:
        if i == '(':
            stack.append(i)
        elif i == ')':
            if not stack:
                nested_parens.append(0)
            else:
                stack.pop()
            nested_parens.append(len(stack))

    return nested_parens

