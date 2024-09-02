from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_depth = []
    diff_stack = []

    for char in paren_string:
        if char == "(":
            diff_stack.append(1)
        elif char == ")":
            if len(diff_stack) == 0:
                raise ValueError("Attempted to close a paren that was never opened")
            else:
                diff_stack.pop()
    if len(diff_stack) > 0:
        raise ValueError("Cannot close a paren that is opened")

    diff_stack = []

    for char in paren_string:
        if char == "(":
            diff_stack.append(1)
        elif char == ")":
            if len(diff_stack) == 0:
                nesting_depth.append(0)
            else:
                nesting_depth.append(diff_stack[-1] - 1)
                diff_stack.pop()

    return nesting_depth

