from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    num_parens_seen = 0
    num_nested_parens = 0
    num_nested_parens_seen = 0
    level = 0
    toReturn = []
    for char in paren_string:
        if char == '(':
            level += 1
            num_nested_parens += 1
            num_nested_parens_seen += 1
        elif char == ')':
            level -= 1
            num_nested_parens_seen -= 1
            num_nested_parens -= 1
        elif char == ' ':
            toReturn.append(num_nested_parens_seen)
    toReturn.append(num_nested_parens)
    return toReturn

