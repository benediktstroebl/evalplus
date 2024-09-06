from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    balanced_string = ''
    paren_list = []
    for i in range(len(paren_string)):
        if paren_string[i] != ' ':
            balanced_string += paren_string[i]

        if balanced_string.count('(') == balanced_string.count(')'):
            if len(balanced_string) > 0:
                paren_list.append(balanced_string)
                balanced_string = ''

    return paren_list

