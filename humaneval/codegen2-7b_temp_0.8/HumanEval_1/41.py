from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    index = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            paren_groups.append(paren_string[:index])
            paren_string = paren_string[index + 1 :]
        else:
            index += 1
    paren_groups.append(paren_string)
    return paren_
