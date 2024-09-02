from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Track the current paren level and max paren level
    curr_level = 0
    max_level = 0

    # Track the open and close parens for this level
    open_parens = 0
    closed_parens = 0

    # Iterate over the input string:
    for char in paren_string:

        # If we close a paren, decrease the count of open parens by one
        if char == ')':
            closed_parens += 1
            if open_parens == 0:
                curr_level -= 1
        # If we open a paren, increase the count of open parens by one
        elif char == '(':
            open_parens += 1
            # After opening a paren, increase the current level of nested parens
            # by 1
            if open_parens > 1:
                curr_level += 1
        # If we see a closing paren, decrease the count of closed parens by 1
        elif char == ')':
            closed_parens -= 1
            # After closing a paren, decrease the current level of nested parens
            # by 1, but also decrease the max level of nested parens
            if open_parens == 0:
                curr_level -= 1
                max_level = max(max_level, curr_level)

    return [max_level, curr_level]

