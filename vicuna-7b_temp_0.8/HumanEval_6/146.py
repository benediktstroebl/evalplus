from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    group_max_nesting = [0] * len(paren_string)
    for i, char in enumerate(paren_string):
        if char == '(':
            group_max_nesting[i] = group_max_nesting[i-1] + 1
        elif char == ')':
            group_max_nesting[i] = group_max_nesting[i+1] - 1
    return group_max_nesting
