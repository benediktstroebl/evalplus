from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []
    stack = []
    depth = 0
    for char in paren_string:
        if char == '(':
            stack.append(depth)
            depth += 1
        elif char == ')':
            depth -= 1
        if depth == 0 and len(stack) > 0:
            if stack[-1] == 0:
                stack.pop()
    return stack[::-1
