from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    max_depth = 0
    output = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            if len(stack) > max_depth:
                max_depth = len(stack)
        else:
            stack.pop()

        if not stack:
            output.append(max_depth)
            max_depth = 0

    return output

