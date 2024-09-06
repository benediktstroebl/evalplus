from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) % 2 != 0:
        raise Exception('Invalid Input')
    elif len(paren_string) == 0:
        return []

    i = 0
    result = []
    while i < len(paren_string):
        j = i
        result.append('')
        while 0 <= j < len(paren_string) and paren_string[j] != ')':
            result[-1] += paren_string[j]
            j += 1
        if 0 <= j < len(paren_string):
            result[-1] += paren_string[j]
        i = j + 1

    return result

