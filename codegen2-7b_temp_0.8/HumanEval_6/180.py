from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    out_array = []

    for group in paren_string.split(' '):
        paren_stack = []

        for char in group:
            if char == '(':
                paren_stack.append(char)
            elif char == ')':
                if paren_stack and paren_stack[-1] == '(':
                    paren_stack.pop()
                else:
                    paren_stack.append(char)

        out_array.append(len(paren_stack))

    return out_
