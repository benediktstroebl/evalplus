from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    depth = 0
    max_depth = 0
    out = []

    for c in paren_string:
        if c == '(':
            stack.append(c)
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif c == ')':
            stack.pop()
            depth -= 1

        if len(stack) == 0:
            out.append(max_depth)
            max_depth = 0

    return out

