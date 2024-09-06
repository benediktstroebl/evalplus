from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens_level = 0
    paren_level = 0
    nested_parens = []
    for char in paren_string:
        if char == '(':
            paren_level += 1
        elif char == ')':
            if paren_level == 1:
                nested_parens.append(nested_parens_level)
                nested_parens_level = 0
            else:
                paren_level -= 1
        else:
            nested_parens_level += 1

    return nested_paren
