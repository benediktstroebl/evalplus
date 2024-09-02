from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_groups = []
    paren_group = ''
    for i, paren in enumerate(paren_string):
        if paren == '(':
            paren_group += paren
            if i!= len(paren_string) - 1 and paren_string[i + 1]!= ')':
                continue
            else:
                paren_groups.append(paren_group)
                paren_group = ''
        elif paren == ')':
            paren_group += paren
            if i!= len(paren_string) - 1 and paren_string[i + 1]!= ')':
                continue
            else:
                paren_groups.append(paren_group)
                paren_group = ''
    return paren_groups
