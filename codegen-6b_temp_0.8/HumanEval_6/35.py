from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    max_depth = 0
    stack = []

    for paren in paren_string.split():
        if paren == '(':
            stack.append('(')
            depth += 1
        elif paren == ')':
            if len(stack) == 0:
                return []
            top = stack.pop()
            while top != '(':
                max_depth = max(depth, max_depth)
                top = stack.pop()
            depth -= 1

    return list(reversed(range(max_depth)))

