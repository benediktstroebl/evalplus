from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    new_parens = []
    current_depth = 0
    for i in range(len(paren_string)):
        char = paren_string[i]
        if char == '(':
            current_depth += 1
        elif char == ')':
            current_depth -= 1
        new_parens.append(current_depth)
    return new_parens

