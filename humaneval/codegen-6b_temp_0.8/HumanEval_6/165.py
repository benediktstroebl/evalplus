from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    max_depth = 0
    nested_parens = []
    for i, paren in enumerate(paren_string):
        if paren == '(':
            nested_parens.append(i)
        elif paren == ')':
            max_depth = max(max_depth, nested_parens.pop())
    return max_depth + 1

