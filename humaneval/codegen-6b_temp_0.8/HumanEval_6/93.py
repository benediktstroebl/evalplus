from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_parens = []
    level_parens = 0
    nested_parens.append(0)

    for paren in paren_string:
        if paren == '(':
            level_parens += 1
            nested_parens.append(level_parens)
        elif paren == ')' and paren_string[-1] != ')':
            level_parens -= 1
            nested_parens.append(level_parens)
        else:
            continue

    return nested_parens

