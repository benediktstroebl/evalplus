from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens_list = paren_string.split()
    for i in range(len(nested_parens_list)):
        nested_parens_list[i] = nested_parens_list[i].count('(') - nested_parens_list[i].count(')')
    return nested_parens_list

