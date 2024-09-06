from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_paren_groups = paren_string.split()
    nested_paren_list = []

    for nested_paren_group in nested_paren_groups:
        if nested_paren_group.count('(') == nested_paren_group.count(')'):
            nested_paren_list.append(
                nested_paren_group.count('(') - nested_paren_group.count(')'))
    return nested_paren
