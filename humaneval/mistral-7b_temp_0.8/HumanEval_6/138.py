from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # We will use a stack to do this
    stack = []
    levels = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        else:
            stack.pop()
            levels.append(len(stack))
    return levels

