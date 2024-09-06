from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # figure out the depth of the substrings between the parentheses
    # We use a stack to keep track of the current depth
    depth = 0
    max_depth = 0
    stack = []

    parens = [0] * len(paren_string)
    for i, character in enumerate(paren_string):
        if character == '(':
            stack.append(i)
        elif character == ')':
            depth += 1
            stack.pop()
        max_depth = max(depth, max_depth)

        if len(stack) == 0:
            parens[i] = max_depth

    return parens

