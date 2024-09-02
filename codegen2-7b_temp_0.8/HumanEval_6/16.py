from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_list = []
    paren_string = paren_string.strip()
    for paren_group in paren_string.split():
        if paren_group[0] == '(':
            new_level = parse_nested_parens(paren_group[1:])
            nested_list.append(len(new_level))
        else:
            nested_list.append(0)
    return nested_
