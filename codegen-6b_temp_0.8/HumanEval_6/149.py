from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depth = 0
    l = len(paren_string)
    paren_stack = []
    for i in range(l):
        if paren_string[i] == '(':
            depth += 1
            paren_stack.append(depth)
            pass
        elif paren_string[i] == ')':
            depth -= 1
            paren_stack.pop()
            pass
    return paren_stack

