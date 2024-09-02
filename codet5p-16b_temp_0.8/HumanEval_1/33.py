from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    groups = []
    temp = []
    for idx, ch in enumerate(paren_string):
        if ch == '(':
            temp.append(ch)
        else:
            if len(temp) == 0:
                groups.append(paren_string[:idx + 1])
                groups.append(paren_string[idx + 1:])
                return groups
            else:
                temp.pop()
                groups.append(''.join(temp))
                temp = [paren_string[idx]]
    if len(temp) > 0:
        groups.append(''.join(temp))
    return groups

