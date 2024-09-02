from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested = 0
    count = [0] * len(paren_string)
    for i, char in enumerate(paren_string):
        if char == '(':
            nested += 1
            count[i] = nested
        elif char == ')':
            nested -= 1
            count[i] = nested
    return count

