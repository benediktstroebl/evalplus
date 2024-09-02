from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack: List[int] = []
    max_level: List[int] = []

    for c in paren_string:
        if c == "(":
            stack.append(0)
        elif c == ")":
            max_level.append(stack.pop())
        else:
            pass

    return max_level

