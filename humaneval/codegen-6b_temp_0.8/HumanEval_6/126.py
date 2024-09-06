from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    curr_paren_stack = []

    for c in paren_string:
        if c == '(':
            curr_paren_stack.append(0)
        elif c == ')':
            curr_paren_stack.pop()
        elif c == '(':
            curr_paren_stack[-1] += 1

    for i in range(len(curr_paren_stack) - 1, -1, -1):
        paren_stack.append(len(curr_paren_stack) - i)

    return paren_stack

