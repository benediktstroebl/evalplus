from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nesting_stack = []
    groups = []

    # For each character in the string
    for char in paren_string:
        # If the character is an open paren,
        if char == '(':
            # Put the character onto the stack
            nesting_stack.append(char)
        # If the character is a closing paren
        elif char == ')':
            # Pop off the stack, until a matching open paren is found
            # If no matching open paren is found, raise an error
            while True:
                if not nesting_stack:
                    raise ValueError("Incorrect string")
                close_paren = nesting_stack.pop()
                if close_paren != '(':
                    raise ValueError("Incorrect string")
                else:
                    break

            groups.append(''.join(nesting_stack))

    # Return the list of groups
    return groups

