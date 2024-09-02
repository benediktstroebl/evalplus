from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Create a set of open parenthesis and a set of closed parenthesis
    open_paren = '('
    close_paren = ')'
    nested_paren = []
    current_level = 0

    for char in paren_string:
        if char == open_paren:
            current_level += 1
        elif char == close_paren:
            current_level -= 1
        elif char == open_paren and current_level > 0:
            nested_paren.append(current_level)

    return nested_paren

