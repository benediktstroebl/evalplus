from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split(' ')
    output = []
    for group in parens:
        stack = []
        for char in group:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(char)
        output.append(len(stack))
    return output
