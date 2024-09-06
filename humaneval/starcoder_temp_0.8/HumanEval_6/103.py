from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    max_depth = []
    # append a default value in case there are no parentheses
    stack.append(-1)
    # append an open parenthesis at the beginning
    stack.append(0)
    for char in paren_string:
        if char == "(":
            stack.append(stack[-1] + 1)
        elif char == ")":
            stack.pop()
            max_depth.append(stack[-1])
    return max_depth
