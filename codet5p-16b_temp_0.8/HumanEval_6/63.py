from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_list = list(paren_string.split(' '))
    nested_parens = []

    for i in range(len(paren_list)):
        if paren_list[i].count('(') == paren_list[i].count(')'):
            nested_parens.append(paren_list[i].count('('))
        else:
            nested_parens.append(paren_list[i].count('(') - paren_list[i].count(')'))

    return nested_parens
