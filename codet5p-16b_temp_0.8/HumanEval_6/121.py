from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    return_list = []
    depth = 0
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            depth += 1
        else:
            depth -= 1
        if depth == 0:
            return_list.append(depth)
            depth = 0
        else:
            return_list.append(depth)
        i += 1

    return return_list
