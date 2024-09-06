from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # return list_of_strings
    balanced_list = []
    current_string = ''
    balance = 0

    for char in paren_string:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        current_string += char

        if balance == 0:
            balanced_list.append(current_string.replace(' ', ''))
            current_string = ''

    return balanced_list

