from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(1)
        elif char == ')':
            if len(stack) == 0:
                result.append(0)
            else:
                top = stack.pop()
                if top == 1:
                    result.append(2)
                elif top == 0:
                    result.append(1)
                else:
                    result.append(0)
                stack.append(top - 1)
        else:
            result.append(1)
    return result

