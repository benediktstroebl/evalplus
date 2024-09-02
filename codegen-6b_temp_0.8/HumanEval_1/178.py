from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = ['']
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            result.append('')
            i += 1
        elif paren_string[i] == ')':
            substring = paren_string[i + 1:len(paren_string)]
            result.append(substring)
            paren_string = paren_string[:i] + paren_string[len(paren_string):]
            i += 1
        else:
            i += 1
    return result

