from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    deepest_level = 0
    deepest_levels = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            deepest_level += 1
            deepest_levels.append(deepest_level)
        elif paren_string[i] == ')':
            deepest_level -= 1
    return deepest_levels

