from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    open_paren = 0
    max_open_paren = 0
    paren_strings = paren_string.split()
    max_parens = []

    for paren in paren_strings:
        for char in paren:
            if char == '(':
                open_paren += 1
                if open_paren > max_open_paren:
                    max_open_paren = open_paren
            elif char == ')':
                open_paren -= 1
        max_parens.append(max_open_paren)
    return max_parens

