from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.strip()
    paren_string = paren_string.replace(' ', '')
    count = 0
    paren_strings = []
    for char in paren_string:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
        if count == 0:
            paren_strings.append(paren_string[:paren_string.index(char)])
            paren_string = paren_string[paren_string.index(char) + 1:]
    return paren
