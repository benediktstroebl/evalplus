from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # main strategy is to simulate a stack where all the opening brackets are pushed
    # and if we find the closing bracket then the topmost element in the stack
    # will be the string we are looking for
    # once we are done reading the string we will just return the stack.
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append('')
        elif char == ')':
            top = stack.pop()
            stack[-1] += '(' + top + ')'
    return stack

