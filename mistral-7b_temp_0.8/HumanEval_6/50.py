from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    levels = 0
    for i, paren in enumerate(paren_string):
        if paren == '(':
            levels += 1
        elif paren == ')':
            levels -= 1
        if i + 1 == len(paren_string):
            result.append(levels)
    return result

