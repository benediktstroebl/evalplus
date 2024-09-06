from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    res = []
    for grp in paren_string.split():
        open_paren_count = 0
        for paren in grp:
            if paren == '(':
                open_paren_count += 1
            elif paren == ')':
                open_paren_count -= 1
        res.append(open_paren_count)

    return res

