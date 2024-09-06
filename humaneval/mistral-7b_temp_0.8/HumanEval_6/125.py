from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    output = []

    paren_stack = []
    max_level = 0

    for group in paren_string.split():
        for char in group:
            if char == '(':
                paren_stack.append(char)
                max_level = max(max_level, len(paren_stack))
            elif char == ')':
                paren_stack.pop()

        output.append(max_level)
        max_level = 0

    return output

