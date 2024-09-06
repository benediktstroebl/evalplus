from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    for group in paren_string.split():
        stack = []
        level = 0
        for c in group:
            if c == '(':
                stack.append(level)
                level += 1
            elif c == ')':
                level = stack.pop()
        result.append(level)
    return result

