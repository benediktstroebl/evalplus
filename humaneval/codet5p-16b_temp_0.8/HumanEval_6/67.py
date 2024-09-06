from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    return_list = []
    current_level = 0
    return_list.append(current_level)

    for char in paren_string:
        if char == '(' and current_level == 0:
            current_level = current_level + 1
            return_list.append(current_level)
        elif char == ')' and current_level > 0:
            current_level = current_level - 1
            return_list.append(current_level)
        elif char == '(':
            current_level = current_level + 1
        elif char == ')':
            current_level = current_level - 1

    return return_list

