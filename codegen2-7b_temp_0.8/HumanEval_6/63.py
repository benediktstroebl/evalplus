from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if len(paren_string) == 0:
        return []

    if paren_string[0]!= '(' or paren_string[-1]!= ')':
        raise ValueError(f'Expecting to start and end with "(" and ")" but got "{paren_string}"')

    nested_list = []

    for paren in paren_string[1:-1]:
        nested_list.append(parse_nested_parens(paren)[0])

    return nested_
