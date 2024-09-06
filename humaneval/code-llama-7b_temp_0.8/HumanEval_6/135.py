from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_paren_depth = 0
    paren_depth_dict = {0: 0}
    # for each character in the paren_string, if it's (, update paren_depth_dict
    # if it's ), update max_paren_depth, and update paren_depth_dict
    # at the end, return the list of max depth of paren for each group
    for char in paren_string:
        if char == "(":
            paren_depth_dict[max_paren_depth + 1] = paren_depth_dict[max_paren_depth] + 1
        if char == ")":
            max_paren_depth += 1
            paren_depth_dict[max_paren_depth] = paren_depth_dict[max_paren_depth - 1] - 1
    return [max_paren_depth for _, max_paren_depth in paren_depth_dict.items()]

