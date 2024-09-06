from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    result = []
    i = 0
    level = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            level += 1
        elif paren_string[i] == ')':
            level -= 1
        if level == 0 and paren_string[i] == ')':
            result.append(i - len(paren_string))
            level = 0
        i += 1
    return result

