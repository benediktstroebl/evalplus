from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    return_list = []
    for i in range(1, len(paren_string)):
        i = i + 1
        if paren_string[i] == '(':
            return_list.append(i + 1)
        else:
            return_list.append(i)
    return return_list

