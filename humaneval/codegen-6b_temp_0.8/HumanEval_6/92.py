from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    parens = []

    for i, p in enumerate(paren_string):
        if p == '(':
            stack.append(i)
        elif p == ')':
            if len(stack) == 0:
                stack.append(i)
            else:
                parens.append(stack.pop())

    if len(stack) != 0:
        return None

    result = []
    for p in parens:
        nest = 1
        for i in range(p-1, -1, -1):
            if paren_string[i] == '(':
                nest += 1
            elif paren_string[i] == ')':
                nest -= 1
                if nest == 0:
                    result.append(i)
                    break

    return result

