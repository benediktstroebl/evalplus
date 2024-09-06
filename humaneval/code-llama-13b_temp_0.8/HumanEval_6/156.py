from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    level = 0
    max_level = 0
    return_list = []

    for paren in paren_string:
        if paren == '(':
            level += 1
        elif paren == ')':
            level -= 1
        else:
            return_list.append(max_level)
            max_level = 0
            level = 0
        max_level = max(max_level, level)
    return_list.append(max_level)

    return return_list

