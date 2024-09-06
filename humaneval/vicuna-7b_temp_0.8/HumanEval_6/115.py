from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    count = 0
    stack = [0]
    output = []

    for char in paren_string:
        if char == '(':
            stack.append(stack[-1] + 1)
        elif char == ')':
            while stack[-1] > 0:
                stack.pop()

        count = count + 1

    while stack:
        output.append(stack[-1])
        stack = stack[:-1]

    return output
