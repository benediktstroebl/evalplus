from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    max_len = 0
    for paren in paren_string:
        if paren == "(":
            stack.append(paren)
        elif paren == ")":
            stack.pop()
            max_len = max(max_len, len(stack))

    return [max_len] * len(paren_string.split())
