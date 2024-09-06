from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """

    # Empty string returns an empty list.
    if paren_string == "":
        return []

    # Each index has a nested parens level, represented as an integer.
    level = 0

    # A list to keep track of the current level of nesting.
    levels = []

    # Set up a parser that will iterate through the given string.
    for char in paren_string:
        # Check if the current character is an opening parenthesis.
        if char == '(':
            # If it is, increase the current level of nesting by one.
            level += 1

        # Check if the current character is a closing parenthesis.
        if char == ')':
            # If it is, decrease the current level of nesting by one.
            level -= 1

        # Check if we need to append the current level to the levels list.
        if level == 0:
            levels.append(0)

    # Return the levels list.
    return levels

