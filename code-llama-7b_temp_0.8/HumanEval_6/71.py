from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Keep track of the highest level of nesting for each group
    # by updating this value as we progress through the string
    highest_level = 0
    max_level = []
    curr_level = 0

    # Iterate through the string one character at a time
    for char in paren_string:
        # If we encounter an opening parenthesis, we have found a new group
        if char == '(':
            curr_level += 1
            # Keep track of the maximum level of nesting for the entire string
            if curr_level > highest_level:
                highest_level = curr_level
        # If we encounter a closing parenthesis, it may have completed
        # a group or it may have been nested within the previous group
        elif char == ')':
            if curr_level == 0:
                # We can't have a closing parenthesis without an opening
                # parenthesis before it
                raise ValueError("No opening parenthesis to close!")
            else:
                curr_level -= 1

        # If we have finished a group, record the deepest level of nesting
        if char == ' ' or char == ')':
            max_level.append(highest_level)
            highest_level = 0

    return max_level

