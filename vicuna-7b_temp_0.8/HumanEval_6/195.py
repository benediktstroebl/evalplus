from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    current_nesting = 0

    for char in paren_string:
        if char == '(':
            if current_nesting == 0:
                nested_parens.append(current_nesting)
                current_nesting += 1
            else:
                current_nesting -= 1
        elif char == ')':
            nested_parens.append(current_nesting)
            current_nesting = nested_parens[-1] + 1

    return nested_parens

