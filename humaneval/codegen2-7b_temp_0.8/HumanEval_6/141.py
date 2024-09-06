from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_level = 0
    max_val = 0
    for i, paren in enumerate(paren_string):
        if paren == '(':
            level = 1
        elif paren == ')':
            level = -1
        else:
            raise ValueError
        level *= -1

        if level > max_level:
            max_level = level
            max_val = i

    return [max_level, max_val + 1, max_level, max_val
