from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Initialize a list to store the maximum level of nesting for each group
    max_nesting = []
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is a '(', add 1 to the maximum nesting
        if char == '(':
            max_nesting.append(max(max_nesting) + 1)
        # If the character is a ')', append the current maximum nesting to the list
        elif char == ')':
            max_nesting.append(max_nesting[-1])
    return max_nesting

