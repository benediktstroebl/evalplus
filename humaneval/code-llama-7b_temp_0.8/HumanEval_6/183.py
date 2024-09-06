from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []

    stack = []
    max_depth = 0
    result = []

    for idx, ch in enumerate(paren_string):
        if ch == "(":
            stack.append(idx)
        elif ch == ")":
            if stack:
                max_depth = max(max_depth, len(stack))
                stack.pop()

    for idx, ch in enumerate(paren_string):
        if ch == "(":
            result.append(max_depth)
        elif ch == ")":
            result.append(result[-1] - 1)

    return result

