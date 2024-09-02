from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    count = 0
    result = []
    for i, c in enumerate(paren_string):
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count == 0:
            result.append(i + 1)
    return result

