from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_nesting = 0
    left = []
    right = []

    for char in paren_string:
        if char == '(':
            left.append(1)
        elif char == ')':
            right.append(1)
        else:
            if left or right:
                max_nesting = max(max_nesting, len(right) - len(left) + 1)

            left = []
            right = []

    if left or right:
        max_nesting = max(max_nesting, len(right) - len(left) + 1)

    return max_nesting

