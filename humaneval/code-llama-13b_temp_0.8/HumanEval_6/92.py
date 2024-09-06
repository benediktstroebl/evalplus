from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    output = []
    for paren_group in paren_string.split():
        paren_stack = []
        max_depth = 0
        for char in paren_group:
            if char == '(':
                paren_stack.append(char)
            elif char == ')':
                if len(paren_stack) == 0:
                    paren_stack.append(char)
                elif len(paren_stack) == 1 and paren_stack[-1] == '(':
                    paren_stack.pop()
                    max_depth += 1
                else:
                    paren_stack.append(char)
        output.append(max_depth)
    return output

