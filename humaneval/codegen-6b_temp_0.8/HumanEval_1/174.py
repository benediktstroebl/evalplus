from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    i = 0
    count = 1
    result = []
    while i < len(paren_string):
        if paren_string[i] == '(':
            count += 1
        elif paren_string[i] == ')':
            count -= 1
        if count == 0:
            result.append(paren_string[i:i + (count + 1) * 2 - 1])
            i += (count + 1) * 2 - 1
        i += 1

    return result

