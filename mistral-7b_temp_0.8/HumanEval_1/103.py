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
    open_braces = 0

    for letter in paren_string:
        if letter == '(':
            open_braces += 1
        elif letter == ')':
            open_braces -= 1

        if open_braces == 0 and letter == ')':
            result.append('')
            continue

        if open_braces == 0 and letter != ')':
            result.append(letter)

        if open_braces != 0:
            result.append(letter)

    return result

