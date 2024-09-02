from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    levels = 0
    result = []

    for ch in paren_string:
        if ch == '(':
            levels += 1
        elif ch == ')':
            levels -= 1
        elif levels == 0 and ch != ' ':
            raise ValueError(f"Unexpected character '{ch}' in string '{paren_string}'")

        result.append(levels)

    return result

