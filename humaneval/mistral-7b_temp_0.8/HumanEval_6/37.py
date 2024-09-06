from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Add the first parentheses to the stack
    paren_stack = [int(paren_string[0])]

    for paren in paren_string[1:]:
        if paren == '(':
            paren_stack.append(paren_stack[-1] + 1)
        else:
            paren_stack.pop()

    return paren_stack

