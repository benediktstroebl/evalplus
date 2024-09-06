from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    current_nesting = 0
    nesting = []
    for c in paren_string:
        if c == '(':
            current_nesting += 1
            nesting.append(current_nesting)
        elif c == ')':
            current_nesting -= 1
            nesting.append(current_nesting)
        else:
            raise Exception(f"Unexpected character {c}.")
    return nesting

