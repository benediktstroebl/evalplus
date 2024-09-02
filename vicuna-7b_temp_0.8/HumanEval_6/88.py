from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return_list = List()

    for char in paren_string:
        if char == '(':
            return_list.append(1)
        elif char == ')':
            current_level = return_list.pop(0)
            return_list.append(current_level * 2)

    return return_list