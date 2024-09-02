from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    #  For each maximum level of nesting, find the depth of each level.
    stack = []
    depth = 0
    for paren in paren_string:
        if paren == '(':
            depth += 1
            stack.append(depth)
        else:
            depth -= 1
            stack.pop()
    return stack

