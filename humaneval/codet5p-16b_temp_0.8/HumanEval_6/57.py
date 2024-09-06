from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if not paren_string:
        return []
    paren_list = paren_string.split()
    max_depth = 1
    depth_list = [1]
    for i in range(len(paren_list)):
        if paren_list[i] == '(':
            depth_list.append(depth_list[-1] + 1)
            if depth_list[-1] > max_depth:
                max_depth = depth_list[-1]
        else:
            depth_list.pop()
    return depth_list

