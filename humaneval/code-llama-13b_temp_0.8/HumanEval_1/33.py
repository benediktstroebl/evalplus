from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string is None:
        raise ValueError('paren_string cannot be None')
    res = []
    count = 0
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            count += 1
        if paren_string[i] == ')':
            count -= 1
        if i + 1 == len(paren_string):
            res.append(paren_string)
        if paren_string[i + 1] == ')' and count == 0:
            res.append(paren_string[:i + 1])
            paren_string = paren_string[i + 1:]
            i = -1
    return res

