from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack: List[int] = []

    for i in range(len(paren_string)):
        level = 0
        if paren_string[i] == '(':
            stack.append(level)
        elif paren_string[i] == ')':
            # Special case: Empty set found
            if len(stack) == 0:
                return [-1]
            top = stack.pop()
            if stack:
                level = stack[-1]
            else:
                level = 0
            if level > 0:
                level -= 1
            else:
                stack.append(level)
                break
    if stack:
        top = stack[-1]
        if top > 0:
            level = top
            stack.append(level)
        else:
            stack.pop()
    return stack

