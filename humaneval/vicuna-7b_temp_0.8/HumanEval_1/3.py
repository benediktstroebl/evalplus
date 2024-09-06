from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    result = []
    current_open = False
    for char in paren_string:
        if char == '(':
            if current_open:
                stack.append(current_open)
            current_open = True
        else:
            if not current_open:
                stack.pop()
                current_open = False
            else:
                result.append(stack.pop())
        if char == ' ':
            current_open = False
        else:
            current_open = True
    return result