from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    group_stack = []
    for char in paren_string:
        if char == '(':
            group_stack.append(char)
        elif char == ')':
            if group_stack:
                group_stack.pop()
            else:
                group_stack.append(char)
    return [len(group_stack) for group_stack in group_stack
