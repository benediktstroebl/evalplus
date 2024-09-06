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
    paren_group = []
    count_braces = 0
    for idx, char in enumerate(paren_string):
        if char == '(':
            count_braces += 1
        elif char == ')':
            count_braces -= 1
            if count_braces < 0:
                paren_groups.append(''.join(paren_group))
                paren_group = []
                count_braces = 0
        else:
            if count_braces == 0:
                paren_group.append(char)
            else:
                paren_group.append(char)
    if count_braces!= 0:
        raise ValueError("Unbalanced braces. Please check the input string.")
    else:
        paren_groups.append(''.join(paren_group))
    return paren_groups
