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
    groups = []
    while i < len(paren_string):
        if paren_string[i] == '(':
            count = 1
            j = i + 1
            while count > 0:
                if paren_string[j] == '(':
                    count += 1
                elif paren_string[j] == ')':
                    count -= 1
                j += 1
            groups.append(paren_string[i:j - 1])
            i = j - 1
        i += 1
    return groups

