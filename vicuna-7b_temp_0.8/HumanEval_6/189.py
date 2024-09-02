from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens: List[str] = []
    for i, c in enumerate(paren_string):
        if c == '(':
            nested_parens.append((i, c))
        elif c == ')':
            nested_parens.pop(nested_parens.index(c))
    return [len(nested) for nested in nested_parens]

