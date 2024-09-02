from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # traverse the string and keep track of the current level of nesting
    current_level = 0
    max_level = 0
    output = []
    for char in paren_string:
        if char == "(":
            current_level += 1
            max_level = max(current_level, max_level)
        elif char == ")":
            current_level -= 1
        if current_level == 0:
            output.append(max_level)
            max_level = 0
    return output

