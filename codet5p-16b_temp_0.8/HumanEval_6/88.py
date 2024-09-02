from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens = paren_string.split()
    nested_parens_list = []
    for i in range(len(nested_parens)):
        if nested_parens[i]!= '(':
            nested_parens_list.append(nested_parens[i])
        else:
            nested_parens_list.append(1)

    max_level = nested_parens_list.index(max(nested_parens_list))
    return nested_parens_list[max_level + 1:]

