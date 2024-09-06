from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    curr_depth = 0
    depth_buffer = []
    paren_stack = []
    for char in paren_string:
        if char == '(':
            paren_stack.append('(')
            curr_depth += 1
        elif char == ')':
            paren_stack.pop()
            curr_depth -= 1
        else:
            continue

        if curr_depth not in depth_buffer:
            depth_buffer.append(curr_depth)

    max_depth = max(depth_buffer)
    for _ in range(max_depth):
        paren_stack.pop()
    return depth_buffer

