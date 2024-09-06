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
        c = paren_string[i]
        if c == '(':
            while c!= ')':
                c = paren_string[i + 1]
                i += 1
                if c == ')':
                    break
        else:
            i += 1
        result.append(paren_string[i:i + 2])
        i += 2
    return result
    
