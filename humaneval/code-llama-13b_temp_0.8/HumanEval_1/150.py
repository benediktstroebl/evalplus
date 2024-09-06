from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # WRITE YOUR CODE AFTER THIS COMMENT BLOCK
    # DON'T FORGET TO RESTORE THE CODE IN THE STARTER FILE
    paren_stack: List[str] = []
    strings: List[str] = []
    for item in paren_string:
        if item == '(':
            paren_stack.append('(')
        elif item == ')':
            paren_stack.pop()
            strings.append(''.join(paren_stack))
    return strings
