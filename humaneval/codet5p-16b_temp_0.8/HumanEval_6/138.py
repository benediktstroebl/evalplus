from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    if paren_string == '':
        return []

    paren_list = list(paren_string.split(' '))
    max_level = max(parse_nested_parens(ele) for ele in paren_list)
    return [max_level] * paren_list.count('(')
