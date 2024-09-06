from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_level = 0
    max_level = 0
    result = []

    for c in paren_string:
        if c == '(':
            paren_level += 1
            if paren_level > max_level:
                max_level = paren_level
        elif c == ')':
            paren_level -= 1
            if paren_level == 0:
                result.append(max_level)
                max_level = 0

    return result
