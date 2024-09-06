from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    for group in paren_string.split():
        start = 0
        max_nesting = 0
        for char in group:
            if char == '(':
                start += 1
                max_nesting = max(max_nesting, start)
            elif char == ')':
                start -= 1
        nested_parens.append(max_nesting)
    return nested_parens
