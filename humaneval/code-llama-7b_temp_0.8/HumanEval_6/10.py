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
            stack.append(char)
        elif char == ')':
            stack.pop()

        if not stack:
            result.append(1)
            stack.append(char)
        elif len(stack) == 1 and stack[-1] != '(':
            result[-1] += 1
            stack.append(char)
    return result

