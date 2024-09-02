from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    list_ = []
    for group in paren_string.split():
        deepest = 0
        level = 0
        for symbol in group:
            if symbol == '(':
                level += 1
            elif symbol == ')':
                level -= 1
            if level > deepest:
                deepest = level
        list_.append(deepest)
    return list_

