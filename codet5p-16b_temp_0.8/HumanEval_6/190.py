from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    paren_string = paren_string.strip()
    if not paren_string:
        return []

    paren_list = list(paren_string)
    nested_parens = []
    while paren_list:
        current_paren = paren_list.pop(0)
        if current_paren == '(':
            nested_parens.append(current_paren)
        elif current_paren == ')' and nested_parens[-1] == '(':
            nested_parens.pop()
        else:
            raise ValueError(f'Invalid paren {current_paren}')

    return nested_parens

