from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []
    nested_list = []
    string_len = len(paren_string)
    for i in range(1, string_len, 2):
        if paren_string[:i].count('(') == paren_string[:i].count(')'):
            nested_list.append(i)
    if nested_list:
        return nested_list + parse_nested_parens(paren_string[1:])
    return [string_len
