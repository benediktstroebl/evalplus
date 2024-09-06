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
        elif len(stack) > 0:
            top = stack.pop()
            if top == "(":
                stack.append(2)
            else:
                stack.append(1)
        else:
            stack.append(0)
    return stack

