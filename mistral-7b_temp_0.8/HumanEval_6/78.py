from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Remove the whitespaces
    paren_string = paren_string.replace(' ', '')

    # Initialize the level of nesting to zero
    level = 0

    # Initialize a list to store the levels of nesting for each of the groups
    levels = []

    # Iterate through the characters of the input string
    for char in paren_string:
        if char == '(':
            level += 1

        if char == ')':
            level -= 1

        # If the level is non-zero, the input string is still being parsed
        if level > 0:
            levels.append(level)

    # Return the list of levels of nesting
    return levels

