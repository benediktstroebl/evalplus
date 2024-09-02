from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Set up a stack to store parenthesis pairs
    stack = []

    # Initialise a list to store final answers
    results = []

    # Iterate through the string, character by character
    for character in paren_string:
        # Add open braces to the stack
        if character == "(":
            stack.append(character)
        # Remove closed braces from the stack
        elif character == ")":
            stack.pop()
        # If the stack is empty and we have a closed brace then we have a valid group
        if not stack and character == ")":
            results.append("".join(stack))
    return results

