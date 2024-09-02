from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    level = 0
    for s in paren_string:
        if s == '(':
            level += 1
            paren_stack.append(level)
        elif s == ')':
            level -= 1
            if level == 0:
                return paren_stack
            else:
                paren_stack.pop()
    return paren_stack

