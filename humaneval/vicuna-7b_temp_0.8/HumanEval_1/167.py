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
    current_open = True
    result = []
    for char in paren_string:
        if char == '(':
            if not current_open:
                result.append(stack.pop())
            stack.append(char)
            current_open = True
        elif char == ')':
            if not current_open:
                result.append(stack.pop())
            current_open = False
        else:
            current_open = False
    result.extend(stack)
    return result

