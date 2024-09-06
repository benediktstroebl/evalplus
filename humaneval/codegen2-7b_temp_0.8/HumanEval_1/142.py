from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    groups = []
    while len(paren_string):
        start_index = paren_string.find('(')
        if start_index == -1:
            groups.append(paren_string)
            break
        else:
            groups.append(paren_string[:start_index])
            paren_string = paren_string[start_index + 1:]
    return groups
