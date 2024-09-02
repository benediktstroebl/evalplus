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
    if paren_string.count('(')!= paren_string.count(')'):
        return []
    if paren_string == '':
        return ['']
    else:
        first_open_paren = paren_string.find('(')
        result = separate_paren_groups(paren_string[:first_open_paren])
        result.append(paren_string[first_open_paren + 1: -1])
        result.extend(separate_paren_groups(paren_string[-1]))
        return result

