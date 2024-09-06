from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Use a list to store all the results
    result = []

    # Use a stack to remember the parentheses we have seen, push and pop them as we go
    stack = []

    # Use a list to remember the indices of the starting parentheses of each group
    start_paren_groups = []

    # Loop over the characters in the string
    for idx, char in enumerate(paren_string):
        # Check if the current character is an open brace
        if char == "(":
            # If there is anything on the stack already, we have a nested group, which we should not be dealing with
            if stack:
                raise ValueError("Nested groups not permitted.")
            # Store the index for this open brace
            start_paren_groups.append(idx)
        # Check if the current character is a close brace
        elif char == ")":
            # Make sure there is a starting brace on the stack
            if not stack:
                raise ValueError("Mismatched parentheses.")
            # Pop the stack and check if there are any remaining parentheses
            stack.pop()
            # If there are no remaining parentheses, we have a complete group
            if not stack:
                # Create the new string for this group
                new_string = paren_string[
                    start_paren_groups.pop() : idx + 1  # noqa: E203
                ]
                # Append the new string to the results
                result.append(new_string)
    # Make sure there are no remaining parentheses on the stack
    if stack:
        raise ValueError("Mismatched parentheses.")
    # Return the results
    return result

