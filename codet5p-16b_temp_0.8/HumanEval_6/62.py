from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens = []

    num_parens_left = 0
    num_parens_right = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            num_parens_left += 1
        elif paren_string[i] == ')':
            num_parens_right += 1
        if num_parens_right == num_parens_left:
            nested_parens.append(i)
            num_parens_left = 0
            num_parens_right = 0

    return nested_parens

