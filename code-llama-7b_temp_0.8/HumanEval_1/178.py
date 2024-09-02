from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    new_string = paren_string.replace(' ', '')
    new_list = []
    counter = 0
    string = ''
    for i in new_string:
        if i == '(':
            counter += 1
            string += i
        if i == ')':
            counter -= 1
            string += i
        if counter == 0:
            new_list.append(string)
            string = ''
    return new_list

