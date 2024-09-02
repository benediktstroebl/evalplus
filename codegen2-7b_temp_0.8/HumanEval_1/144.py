from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_index = 0
    paren_strings: List[str] = []
    while start_index < len(paren_string):
        end_index = paren_string.find(')', start_index)
        if end_index == -1:
            paren_strings.append(paren_string[start_index:])
            break
        paren_strings.append(paren_string[start_index:end_index])
        start_index = end_index + 1
    return paren_
