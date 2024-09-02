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
    current = []
    nest = 0
    for char in paren_string.replace(' ', ''):
        if char == '(':
            nest += 1
        elif char == ')':
            nest -= 1
        current.append(char)
        if nest == 0 and current != ['(', ')']:
            result.append(''.join(current))
            current = []
    return result

