from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens_list = paren_string.split(" ")
    max_depth_list = []
    for paren in parens_list:
        depth = 0
        depth_count = 0
        for char in paren:
            if char == '(':
                depth += 1
            else:
                depth -= 1

            if depth == 0:
                depth_count += 1
        max_depth_list.append(depth_count)
    return max_depth_list

