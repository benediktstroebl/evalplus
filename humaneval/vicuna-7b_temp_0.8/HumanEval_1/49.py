from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # your code here
    # a simple approach is to use a stack to keep track of the open and close parentheses
    # as you see them, and when you see an odd number of open parentheses, you push a string
    # to the stack and return it. when you see an even number of open parentheses, you pop
    # from the stack and return it.
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) % 2 == 0:
                result.append(stack.pop())
            else:
                result.append(stack.pop())
                result.append(stack.pop())
    return result
