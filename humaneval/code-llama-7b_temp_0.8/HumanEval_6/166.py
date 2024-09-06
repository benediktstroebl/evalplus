from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    open_counter = 0
    max_depth = 0
    max_depth_list = []
    for char in paren_string:
        if char == '(':
            open_counter += 1
            if open_counter > max_depth:
                max_depth = open_counter
        elif char == ')':
            open_counter -= 1
        if open_counter == 0:
            max_depth_list.append(max_depth)
            max_depth = 0

    return max_depth_list

