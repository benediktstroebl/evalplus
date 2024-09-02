from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = paren_string.split()
    nesting_levels = []
    for paren in paren_list:
        nested_levels = []
        for i in range(len(paren)):
            if paren[i] == '(':
                nested_levels.append(1)
            elif paren[i] == ')':
                nested_levels[-1] -= 1
        nesting_levels.append(max(nested_levels))
    return nesting_levels

