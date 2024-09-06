from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split()
    max_depth = [0] * len(parens)
    max_depth[0] = 1

    for i in range(1, len(parens)):
        nested_parens = 1
        curr_paren = parens[i]
        for j in range(0, i):
            prev_paren = parens[j]
            nested_parens = nested_parens + max_depth[j] if curr_paren[j] == ')' else nested_parens - 1
        max_depth[i] = nested_parens

    return max_depth

