from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_groups = []
    level = 0
    for paren_string in paren_string.split(' '):
        paren_groups.append([])
        for paren in paren_string:
            if paren == '(':
                level += 1
            elif paren == ')':
                level -= 1
            if level == 0:
                paren_groups[-1].append(paren)
    return paren_groups

