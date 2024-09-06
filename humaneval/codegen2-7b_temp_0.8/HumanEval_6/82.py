from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    nested_parens = 0
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if not stack:
                raise ValueError("Invalid parentheses string: '{}'".format(paren_string))
            stack.pop()
            if not stack:
                nested_parens += 1
        else:
            raise ValueError("Invalid parentheses string: '{}'".format(paren_string))
    return [nested_parens]
