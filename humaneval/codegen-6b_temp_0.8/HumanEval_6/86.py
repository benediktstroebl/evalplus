from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    n = len(paren_string)
    n_stack = 0
    for i in range(n):
        if paren_string[i] == '(':
            n_stack += 1
        elif paren_string[i] == ')':
            n_stack -= 1
        elif paren_string[i] == ' ':
            result.append(n_stack)
    return result

