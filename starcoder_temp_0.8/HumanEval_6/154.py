from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    paren_pairs = []
    for parens in paren_string.split():
        level = 0
        for char in parens:
            if char == '(':
                level += 1
            elif char == ')':
                level -= 1
            if level < 0:
                raise ValueError('Invalid input')
        paren_pairs.append(level)
    return paren_pairs

