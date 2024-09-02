from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack: List[int] = []
    max_level = 0
    groups = paren_string.strip().split(" ")
    for group in groups:
        for char in group:
            if char == "(":
                stack.append(1)
            elif char == ")":
                if stack:
                    stack.pop(-1)
                else:
                    stack.append(0)
        max_level = max(max_level, sum(stack))
        stack = [1]
    return [max_level] * len(groups)

