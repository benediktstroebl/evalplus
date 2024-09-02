from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    stack = []
    result = []
    for paren_string in paren_string.split():
        if not paren_string:
            continue
        elif paren_string == '(':
            stack.append(paren_string)
        elif paren_string == ')':
            if stack:
                stack.pop()
            else:
                result.append(len(stack))
    if stack:
        raise ValueError(paren_string)
    return result
