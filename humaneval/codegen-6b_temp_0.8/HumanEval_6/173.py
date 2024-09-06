from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level = 0
    level_list = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            level += 1
        elif paren_string[i] == ')':
            level -= 1
        level_list.append(level)
    return level_list

