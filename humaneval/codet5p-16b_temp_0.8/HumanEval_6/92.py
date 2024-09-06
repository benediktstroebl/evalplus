from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split()
    paren_stack = []
    max_depth = 0
    for i in paren_list:
        if i == '(':
            paren_stack.append('(')
            if len(paren_stack) > max_depth:
                max_depth = len(paren_stack)
        elif i == ')':
            paren_stack.pop()
    return [max_depth]

