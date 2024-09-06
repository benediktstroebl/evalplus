from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.split()
    deepest_nesting = []

    for nested_paren in paren_string:
        current_nesting = 0
        for char in nested_paren:
            if char == '(':
                current_nesting += 1
            elif char == ')':
                current_nesting -= 1
        deepest_nesting.append(current_nesting)

    return deepest_nesting
