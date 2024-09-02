from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    depth_dict = {}
    for index, parenthesis in enumerate(paren_string):
        if parenthesis == '(':
            depth_dict[index] = 1
            max_depth = max(max_depth, depth_dict[index])
        elif parenthesis == ')':
            last_index = index - 1
            last_depth = depth_dict[last_index]
            depth_dict[index] = last_depth + 1
            max_depth = max(max_depth, depth_dict[index])
    return [max_depth, max_depth - depth_dict[last_index]]

