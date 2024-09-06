from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens_list: List[int] = []
    curr_level_index: int = 0
    for char in paren_string:
        if char == "(":
            nested_parens_list.append(curr_level_index)
            curr_level_index += 1
        elif char == ")":
            curr_level_index -= 1
    nested_parens_list.append(curr_level_index)
    return nested_parens_list
