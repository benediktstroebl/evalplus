from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []
    stack = []
    max_depth = 0
    for paren in paren_string:
        if paren == '(':
            stack.append(0)
            max_depth = max(max_depth, len(stack))
        elif paren == ')':
            if len(stack) == 0:
                return []
            stack.pop()

    return max_depth

