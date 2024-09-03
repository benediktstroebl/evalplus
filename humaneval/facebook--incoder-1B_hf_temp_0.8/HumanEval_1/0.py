from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    paren_position = 0
    for index, char in enumerate(paren_string):
        if char == ')':
            if index == paren_position:
                result.append(paren_string[paren_position:index])
            paren_position = index + 1
        else:
            result.append(char)
    return result

