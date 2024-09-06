from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_stack = []
    nesting = 0
    nesting_level: int = 0
    for char in paren_string:
        if char == '(':
            nesting_level += 1
            nesting_stack.append(nesting_level)
            nesting += 1
        elif char == ')':
            nesting_level -= 1
            nesting_stack.append(nesting_level)
            nesting -= 1
    return nesting_stack

