from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = [0]
    result = []
    for item in paren_string.split():
        if item.startswith('('):
            stack.append(stack[-1] + 1)
        elif item.endswith(')'):
            stack.pop()
            result.append(stack[-1])
    return result
