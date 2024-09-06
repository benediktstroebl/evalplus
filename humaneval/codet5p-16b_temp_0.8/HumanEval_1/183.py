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
        return ['']
    else:
        if paren_string[0] == ')':
            return ['('] + separate_paren_groups(paren_string[1:])
        elif paren_string[0] == '(':
            first_group = separate_paren_groups(paren_string[1:])
            last_group = separate_paren_groups(paren_string[:-1])
            return first_group + [')'] + last_group
        else:
            return ['('] + separate_paren_groups(paren_string[1:])

