from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack: List[str] = []
    deepest = 0
    result: List[int] = []

    for char in paren_string:
        if char == "(":
            stack.append(char)
            if len(stack) > deepest:
                deepest = len(stack)
        if char == ")":
            stack.pop()
    for deep in range(deepest, 0, -1):
        result.append(deep)

    return result

