from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens_string = paren_string.strip()
    result = [0] * len(parens_string)
    max_level = 0
    for i, paren in enumerate(parens_string):
        if paren == '(':
            max_level = max(max_level, result[i-1] + 1)
        elif paren == ')':
            max_level = max(max_level, result[i-1] - 1)
        result[i] = max_level
    return result

