from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    closure = 0
    mapping = {b: a for a, b in enumerate('({[')}

    result = []
    for c in paren_string:
        if c == '(':
            closure += 1
        elif c == ')':
            closure -= 1
        elif c == '[':
            closure += 1
        elif c == ']':
            closure -= 1
        result.append(closure)
    return result

