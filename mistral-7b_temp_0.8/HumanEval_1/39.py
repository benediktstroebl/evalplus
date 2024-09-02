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
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            result.append('')
            j = i + 1
            while j < len(paren_string):
                if paren_string[j] == ')':
                    result[-1] += paren_string[i + 1:j]
                    i = j + 1
                    break
                else:
                    j += 1
        else:
            i += 1
    return result
