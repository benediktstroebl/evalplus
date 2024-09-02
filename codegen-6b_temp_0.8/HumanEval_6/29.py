from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested_level = 0
    parens = []
    for i in range(len(paren_string)):
        paren = paren_string[i]
        if paren == '(':
            nested_level += 1
            parens.append(nested_level)
        elif paren == ')':
            nested_level -= 1
            parens.append(nested_level)
    return parens

