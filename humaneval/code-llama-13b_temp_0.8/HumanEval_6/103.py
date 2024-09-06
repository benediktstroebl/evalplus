from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    output_list = []
    for group in paren_string.split(' '):
        if group.count('(') == group.count(')'):
            output_list.append(1)
        else:
            output_list.append(group.count('(') - group.count(')') + 1)
    return output_list

