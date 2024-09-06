from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if paren_string[0]!= '(' or paren_string[-1]!= ')':
        raise ValueError("Incorrect input, you have to enter parentheses only.")

    parens_stack = []
    for char in paren_string:
        if char == '(':
            parens_stack.append('(')
        elif char == ')':
            if len(parens_stack) == 0 or parens_stack.pop()!= '(':
                raise ValueError("Incorrect input, you have to enter parentheses only.")
    return len(parens_stack)
