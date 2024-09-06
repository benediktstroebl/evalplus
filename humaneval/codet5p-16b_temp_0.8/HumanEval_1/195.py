from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string.count('(') == 0:
        return [paren_string]
    groups = []
    inside = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            if i == 0 or paren_string[i-1] =='':
                inside = []
            inside.append(paren_string[i])
        elif paren_string[i] == ')':
            if i == 0 or paren_string[i-1] =='':
                inside.append(paren_string[i])
                groups.append(''.join(inside))
            else:
                inside.append(paren_string[i])
        i += 1
    return groups

