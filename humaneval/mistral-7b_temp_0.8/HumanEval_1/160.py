from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Use the following braces for balancing
    brace_map = {'{': '}', '[': ']', '(': ')'}

    # An empty stack
    brace_stack = []

    # Separate groups in the string
    separate_groups = []

    # For each character in the input string
    for char in paren_string:

        # If the character is not a brace, add the character to the group
        if char not in brace_map:
            separate_groups[-1] += char

        # If the character is a brace
        else:

            # If the current character is an opening brace, push it to the stack
            if char in brace_map:
                brace_stack.append(char)

            # If the current character is a closing brace
            else:

                # If the current character matches the top of the stack
                if brace_map[brace_stack[-1]] == char:
                    brace_stack.pop()

                # If the current character doesn't match the top of the stack
                else:
