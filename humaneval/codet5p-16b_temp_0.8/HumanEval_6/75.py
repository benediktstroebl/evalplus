from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    groups = paren_string.split()
    for group in groups:
        depth = 0
        for paren in group:
            if paren == '(':
                depth += 1
            elif paren == ')':
                depth -= 1
        stack.append(depth)
    return stack

