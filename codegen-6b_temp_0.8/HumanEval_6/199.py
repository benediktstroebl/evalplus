from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting = 0  # number of levels of nesting of parentheses
    nested_parens: List[bool] = [False] * len(paren_string)

    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            nesting += 1
            nested_parens[i] = nesting
        elif paren_string[i] == ")":
            if nested_parens[i - 1] > 0:
                nesting -= 1
                nested_parens[i] = nesting

    return nested_parens

