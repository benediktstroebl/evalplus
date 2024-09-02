from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Define the stack
    stack = []
    # For each character in the input string
    for c in paren_string:
        # If the character is an open brace
        if c == '(':
            # Push the open brace to the stack
            stack.append(c)
        # If the character is a close brace
        elif c == ')':
            # If the top of the stack is a open brace
            if not stack:
                return []
            # pop the top of the stack
            c = stack.pop()
            # If the popped character is a close brace
            if c == ')':
                continue
            # If the popped character is a open brace
            elif c == '(':
                stack.append(c)
            # If the popped character is not a close brace or an open brace
            else:
                return []
    # If the stack is empty, this means that the input string doesn't have any balanced parentheses,
    # so the function should return an empty list
    return []

