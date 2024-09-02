from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove all spaces in the input string
    paren_string = paren_string.replace(" ", "")

    # Maintain a stack to store opening parenthesis. If a closing brace is encountered and stack is empty,
    # ignore that brace
    stack = []

    # Create a list of separated groups
    separated_groups = []

    # Iterate through the paren string
    for char in paren_string:

        # If an opening brace is encountered, push it to the stack
        if char == "(":
            stack.append(char)

        # If a closing brace is encountered, pop the corresponding opening brace from the stack
        elif char == ")":

            # If the stack is empty, this closing brace doesn't match an opening brace
            if len(stack) == 0:
                continue

            # If the stack is not empty, append the group of nested parentheses to separated_groups
            else:
                separated_groups.append("".join(stack) + char)
                stack.pop()

    return separated_groups

