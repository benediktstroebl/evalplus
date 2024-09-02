from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # base case
    if not paren_string:
        return []

    depths = []

    # stack to keep track of the depth of parentheses
    stack = []
    for char in paren_string:
        if char == "(":
            stack.append(char)
        elif char == ")":
            # Remove the oldest opening parenthesis
            stack.pop()
            depths.append(len(stack))

    return depths

