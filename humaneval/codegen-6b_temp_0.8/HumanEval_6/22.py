from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    depth = 0
    for i in paren_string:
        if i == ')':
            if stack and stack[-1](i) == '(':
                stack.pop()
            else:
                stack.append(i)
        elif i == '(':
            stack.append(i)
        else:
            continue

    return list(reversed(stack))

