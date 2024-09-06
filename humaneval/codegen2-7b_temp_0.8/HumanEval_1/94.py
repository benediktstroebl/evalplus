from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    left_paren = paren_string.count('(')
    right_paren = paren_string.count(')')
    left_paren_to_right = left_paren - right_paren
    output = []
    current_string = ''

    for i in range(len(paren_string)):
        current_string += paren_string[i]
        if paren_string[i] == '(':
            left_paren += 1
        elif paren_string[i] == ')':
            right_paren += 1

    return
