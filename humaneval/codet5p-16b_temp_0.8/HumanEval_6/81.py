from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    stack = []
    max_depth = 0
    nested_paren_depth_list = []
    for idx, char in enumerate(paren_string):
        if char == '(':
            stack.append(idx)
            if len(stack) > max_depth:
                max_depth = len(stack)
        if char == ')':
            last_idx_of_nested_paren = stack.pop()
            nested_paren_depth_list.append(idx - last_idx_of_nested_paren)

    return nested_paren_depth_list

