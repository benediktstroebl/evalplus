from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Push a new empty string to the output stack
    output_stack = []
    output_stack.append("")

    # Insert the input string into the output stack
    # The idea here is to insert the braces from the input string into the stack
    # and if it is a closing brace, pop from the output stack and insert it as well
    for char in paren_string:
        if char == "(":
            # If we found an opening brace, push that to the output stack
            output_stack.append(char)
        elif char == ")":
            # If we found a closing brace, pop the top of the output stack and insert it to the stack
            # Popping from the output stack works like removing the closing brace from the input string
            output_stack.pop()
            output_stack.append(char)

    # Return the output stack
    return output_stack

