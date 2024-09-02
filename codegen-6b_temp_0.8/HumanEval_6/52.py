from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_list = []
    for i in paren_string.split():
        if (len(i) == 1):
            paren_list.append(0)
        else:
            paren_list.append(len(i))
    current_level = paren_list.pop(0)
    max_level = 0
    while paren_list:
        current_level += 1
        max_level = max(max_level, current_level)
        current_level += paren_list.pop(0)
    return [max_level, current_level]

