from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    for i, char in enumerate(paren_string):
        if char == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return [0]
            else:
                stack.pop()
    if len(stack)!= 0:
        return [0]
    else:
        return stack
