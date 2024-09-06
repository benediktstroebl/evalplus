from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    for c in paren_string:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0:
                raise ValueError("Missing opening parenthesis")
            if stack.pop()!= "(":
                raise ValueError("Mismatched closing parenthesis")
    return [len(stack)] + [len(stack) + 1] + [0] + [len(stack) + 2] + [0
