from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    nesting = 0
    current_nesting = 0

    output = []

    for char in paren_string:
        if char == '(':
            current_nesting += 1
            nesting = max(nesting, current_nesting)
            paren_stack.append(char)
        elif char == ')':
            current_nesting -= 1
            paren_stack.pop()
        else:
            output.append(current_nesting)

    output.append(nesting)
    return output

