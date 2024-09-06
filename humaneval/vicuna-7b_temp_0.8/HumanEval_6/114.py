from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_list = []
    for inner_paren in paren_string.replace('(', '').replace(')', '').split():
        # inner paren is a group of nested parentheses
        if '(' in inner_paren:
            # if the inner paren has nested parentheses, add it to the list
            nested_list.extend(parse_nested_parens(inner_paren))
        else:
            # otherwise, add the level of nesting to the list
            nested_list.append(1)
    return nested_list
