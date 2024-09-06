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
    current = []
    for char in paren_string:
        if char == '(':
            stack.append(current)
            current = []
        elif char == ')':
            current.append(stack.pop())
            if not current or len(current) == 1:
                result.append('')
            else:
                result.append(current)
                current = []
        elif char == ' ':
            current.append(char)
        else:
            current.append(char)
    if current:
        result.append(current)
    return result

