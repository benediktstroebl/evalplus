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
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            result.append(paren_string[i])
        elif paren_string[i] == ')':
            result.pop()

        if len(result) == 0:
            result.append(paren_string[i])
    return result

