from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    parens = paren_string.split(' ')
    levels_of_nesting = []
    for paren in parens:
        current_level = 0
        for char in paren:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            else:
                raise ValueError('Unexpected character: ', char)
            if current_level < 0:
                raise ValueError('Too many closed parentheses: ', char)
        levels_of_nesting.append(current_level)
    return levels_of_nesting
