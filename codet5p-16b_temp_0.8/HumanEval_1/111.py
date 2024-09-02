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

    paren_groups = []
    current_group = paren_string
    open_parens = 0
    for i in range(len(current_group)):
        if current_group[i] == '(':
            open_parens += 1
        elif current_group[i] == ')':
            open_parens -= 1
            if open_parens == 0:
                current_group = current_group[:i + 1]
                paren_groups.append(current_group)
                current_group = ''
                open_parens = 0
    if len(current_group) > 0:
        paren_groups.append(current_group)

    return paren_groups

