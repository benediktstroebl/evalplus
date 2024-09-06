from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    cur_level = 0
    for paren in paren_string:
        if paren == '(':
            cur_level += 1
        elif paren == ')':
            cur_level -= 1
        if cur_level < 0:
            break
        if cur_level > 0:
            nested_parens.append(cur_level)
    return nested_paren
