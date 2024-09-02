from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) < 1:
        return []

    stack = []
    max_depth = 0
    i = 0

    while i < len(paren_string):
        if paren_string[i] == "(":
            stack.append(i)
            max_depth = max(max_depth, len(stack))
        elif paren_string[i] == ")":
            # Find the last opening parenthesis and pop off in the stack
            stack.pop()
        i += 1

    return max_depth

