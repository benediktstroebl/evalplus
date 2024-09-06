from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_stack = []
    depth_stack = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            paren_stack.append(i)
            depth_stack.append(0)
        elif paren_string[i] == ')':
            last_parenthesis = paren_stack.pop()
            depth = depth_stack.pop()
            depth_stack[-1] = max(depth, depth_stack[-1])
            if paren_stack:
                paren_stack[-1] = last_parenthesis
    return depth_stack

