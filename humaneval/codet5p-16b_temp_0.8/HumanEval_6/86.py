from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    max_depth = 0
    for c in paren_string:
        if c == '(' and len(stack) > max_depth:
            stack.append(1)
            max_depth = max(max_depth, len(stack))
        elif c == ')' and len(stack) > 0:
            stack.pop()

    return list(map(lambda x: len(stack), stack))

