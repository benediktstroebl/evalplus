from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    nested = []

    # Initialize the index to the first index of the string
    idx = 0

    # This while loop will iterate through the string until the index reaches the end
    while idx < len(paren_string):
        # Use the index to get the current character
        char = paren_string[idx]

        # Check if the character is a left parenthesis '('
        if char == '(':
            # If so, increment the index by 1 to move to the next character
            idx += 1

            # Call the function recursively with the updated index
            # and append the return value to the nested list
            nested.append(parse_nested_parens(paren_string[idx:]))

        # Check if the character is a right parenthesis ')'
        elif char == ')':
            # If so, increment the index by 1 to move to the next character
            idx += 1

            # Pop the last element off the nested list
            # This is the maximum level of nesting for the current group
            nested.pop()

        # If the character is not
