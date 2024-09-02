from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    parens_dict = {}
    depth = 0

    for i, char in enumerate(paren_string):
        if char == "(":
            depth += 1
            parens_dict[i] = depth
        elif char == ")":
            depth -= 1

    max_depth = max(list(parens_dict.values()))
    group_i = [k for k, v in parens_dict.items() if v == max_depth]

    return group_i


    # def get_min_depth(string: str) -> int:
    #     """ Input to this function is a string representing multiple groups for nested parentheses separated by spaces.
    #     For each of the group, output the deepest level of nesting of parentheses.
    #     E.g. (()()) has maximum two levels of nesting while ((())) has three.
    #     >>> get_min_depth('(()()) ((())) () ((())())')
    #     2
    #     """
    #     depth = 0
    #     depth_dict = {}

    #     for i, char in enumerate(string):
    #         if char == "(":
    #             depth += 1
    #             depth_dict[i] = depth
    #         elif char == ")":
    #             depth -= 1

    #     max_depth = max(list(depth_dict.values()))
    #     group_i = [k for k, v in depth_dict.items() if v == max_depth]

    #     return group_i

    #     # depth = 0

    #     # for i, char in enumerate(string):
    #     #     if char == "(":
    #     #         depth += 1
    #     #     elif char == ")":
    #     #         depth -= 1

    #     # return depth

