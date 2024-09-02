from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    level_of_nesting = 0
    result = []
    for paren in paren_string:
        if paren == '(':
            level_of_nesting += 1
        elif paren == ')':
            level_of_nesting -= 1
        if level_of_nesting == 0:
            result.append(level_of_nesting)
    return result

