from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    nested_parens: List[int] = []
    current_level: int = 0
    for char in paren_string:
        if char == '(':
            current_level += 1
        elif char == ')':
            current_level -= 1
            if current_level < 0:
                raise ValueError('Invalid parentheses')
        else:  # if char ==''
            if current_level > len(nested_parens):
                nested_parens.append(current_level)
            else:
                nested_parens[current_level] += 1
    return nested_parens
