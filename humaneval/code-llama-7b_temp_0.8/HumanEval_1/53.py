from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    if len(paren_string) == 2:
        return [paren_string]

    result = []
    i = 1
    while i < len(paren_string) - 1:
        if paren_string[i] == '(':
            j = i
            while paren_string[j] != ')':
                j += 1
            if j == i:
                result.append(paren_string[i: j + 1])
                i = j + 1
            else:
                result.append(paren_string[i: j])
                i = j + 1
        else:
            i += 1
    if i < len(paren_string):
        result.append(paren_string[i:])
    return result

