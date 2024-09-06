from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return_list = []
    for char in paren_string:
        if char == '(':
            return_list.append(1)
        elif char == ')':
            return_list.append(0)
        elif char == ' ':
            return_list[-1] = return_list[-1] * 2  # double the length of the group
        elif char == '(':
            return_list[-1] = return_list[-1] * 2  # double the length of the group
    return return_list

