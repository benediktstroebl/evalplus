from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    count = 0
    result = []
    tmp = ''

    for paren in paren_string:
        if paren == '(':
            count += 1
            tmp += paren
        if paren == ')':
            count -= 1
            tmp += paren
            if count == 0:
                result.append(tmp)
                tmp = ''
    return result

