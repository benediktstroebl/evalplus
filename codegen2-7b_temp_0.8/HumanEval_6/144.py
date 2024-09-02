from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = 0
    level = 0
    for i, ch in enumerate(paren_string):
        if ch == '(':
            nested_parens += 1
            if nested_parens == 1:
                level = i
        elif ch == ')':
            nested_parens -= 1
            if nested_parens == 0 and level!= i:
                level = i
    return [level, nested_parens]
