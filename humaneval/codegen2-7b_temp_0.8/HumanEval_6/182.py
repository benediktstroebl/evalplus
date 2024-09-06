from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []

    result = []

    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            stack = []
            while paren_string[i]!= ')':
                stack.append(paren_string[i])
                i += 1
            i += 1
            while len(stack)!= 0:
                result.append(stack.pop())
        else:
            i += 1

    return result
