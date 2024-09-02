from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    assert paren_string.strip() == paren_string and paren_string.lstrip() == paren_string
    result = []
    current = ''
    for char in paren_string:
        if char == '(':
            if current != '':
                result.append(current)
                current = ''
        elif char == ')':
            if current != '':
                result.append(current)
                current = ''
        else:
            current += char
    if current != '':
        result.append(current)
    return result

