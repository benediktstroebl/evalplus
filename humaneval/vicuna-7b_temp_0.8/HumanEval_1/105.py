from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # This will use a stack to keep track of the current open brace and closing brace.
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if len(stack) > 0:
                # pop the last open brace from the stack
                result.append(stack.pop())
            stack.append(')')
        elif char == ' ':
            # ignore spaces
            pass
        else:
            # this is an error, so we need to print the error message and exit
            print("Invalid input:", paren_string)
            return None
    # We should now have a list of closing braces that we can convert into a list of groups
    return result