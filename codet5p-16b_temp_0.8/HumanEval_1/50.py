from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = []
    open_paren = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(' and open_paren == 0:
            open_paren = 1
        elif paren_string[i] == ')' and open_paren == 1:
            open_paren = 0
            paren_list.append(paren_string[:i + 1])
            paren_string = paren_string[i + 1:]
        elif open_paren == 1:
            continue
        else:
            continue
    return paren_list

