from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint: use stacks
    # Parentheses stack
    stack = []
    # Result list
    result = []
    # Index of a current group
    current = 0
    # Iterate over the string
    for index, char in enumerate(paren_string):
        # If it is an open brace
        if char == "(":
            # Push the index to the stack
            stack.append(index)
        # If it is a close brace
        if char == ")":
            # Pop the last index from the stack
            start = stack.pop()
            # Calculate the length of the current group
            length = index - start + 1
            # Add the group to the result
            result.append(paren_string[start: start + length])
    # Return the result
    return result

