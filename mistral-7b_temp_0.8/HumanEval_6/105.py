from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    lvl = 0
    lvl_list = []

    for char in paren_string:
        if char == '(':
            lvl += 1
        elif char == ')':
            lvl -= 1
        if lvl > lvl_list[-1]:
            lvl_list.append(lvl)
    return lvl_list
