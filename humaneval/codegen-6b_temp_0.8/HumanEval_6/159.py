from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = []
    index = 0
    open_count = 0
    close_count = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            open_count += 1
        elif paren_string[index] == ')':
            close_count += 1
        if open_count == close_count:
            levels.append(open_count)
            open_count = 0
            close_count = 0
        index += 1
    return levels

