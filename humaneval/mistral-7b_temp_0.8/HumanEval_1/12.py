from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Here's your code!
    paren_list = []
    counter = 0
    for i in paren_string:
        if i == '(':
            counter += 1
        elif i == ')':
            counter -= 1
        if counter == 0:
            paren_list.append('(' + paren_string[0:i] + ')')
    return paren_list
