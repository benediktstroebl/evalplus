from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_list = []
    for opening_paren in paren_string.strip('').replace(')', '').replace('(', '').replace(')', '').split(' '):
        if '(' in opening_paren:
            nested_list.append(int(opening_paren.split('(')[0]) + 1)
        else:
            nested_list.append(1)
    return nested_list
