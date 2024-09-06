from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split()
    max_level = 0
    for i in paren_list:
        level = 0
        for j in range(len(i)):
            if i[j] == '(':
                level += 1
            elif i[j] == ')':
                level -= 1
            if level < 0:
                break
        if level > max_level:
            max_level = level
    return [max_level]

