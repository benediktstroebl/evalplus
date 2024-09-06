from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    nr_open = 0
    list_of_groups = []
    while True:
        i = 0
        while i < len(paren_string):
            if paren_string[i] == '(':
                nr_open += 1
            elif paren_string[i] == ')':
                nr_open -= 1
            if nr_open == 0 and i == len(paren_string) - 1:
                list_of_groups.append(paren_string[0:i+1])
                break
            i += 1
        if nr_open == 0:
            break
        paren_string = paren_string[i+1:]
    return list_of_groups

