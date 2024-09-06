from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nesting_levels = []
    for char in paren_string:
        if char == '(':
            nesting_levels.append(1)
        elif char == ')':
            nesting_levels.append(nesting_levels.pop())
        else:
            raise ValueError(f"Invalid character '{char}' encountered in string '{paren_string}'")
    return nesting_levels

