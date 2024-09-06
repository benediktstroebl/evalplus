from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Init variables
    max_level = 0
    max_levels = []

    # Iterate through each character in the paren_string
    for char in paren_string:
        # For each open paren, increment the max_level
        if char == "(":
            max_level += 1
        # For each close paren, decrement the max_level and
        # add the max_level to max_levels if max_level == 0
        elif char == ")":
            max_level -= 1
            if max_level == 0:
                max_levels.append(max_level)

    return max_levels

