from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Open and Close parentheses are balanced in a group
    # Check for nesting

    # Solution:
    # 1. Find the start of the first un-nested group.
    # 2. Scan to the end of the group.
    # 3. Find the start of the next group.
    # 4. Repeat.

    # List of un-nested groups
    groups = []

    # Un-nested group
    current_group = ''

    # Current position
    current_pos = 0

    while current_pos < len(paren_string):
        # Keep looking for the next un-nested group
        while current_pos < len(paren_string) and paren_string[current_pos] != '(':
            current_pos += 1

        if current_pos >= len(paren_string):
            break

        # Store the opening parenthesis
        current_group += paren_string[current_pos]

        # Continue to the end of the group
        while current_pos < len(paren_string) and paren
