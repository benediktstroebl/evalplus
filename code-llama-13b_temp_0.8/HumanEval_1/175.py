from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_paren = ''
    inside_paren = False

    for char in paren_string:
        if char == '(':
            inside_paren = True
        elif char == ')':
            inside_paren = False
            current_paren += char
            result.append(current_paren)
            current_paren = ''
        elif inside_paren:
            current_paren += char

    return result

