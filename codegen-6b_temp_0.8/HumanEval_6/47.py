from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    paren_level = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            paren_stack.append(paren_level)
            paren_level += 1
        elif paren_string[i] == ')':
            paren_level -= 1
            paren_stack.pop()
    return paren_stack

