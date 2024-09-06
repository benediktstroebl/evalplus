from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    list_of_paren_groups = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            k = i
            while k < len(paren_string) and paren_string[k] == '(':
                k += 1
            list_of_paren_groups.append(paren_string[i:k])
            i = k - 1
        i += 1
    return list_of_paren_groups

