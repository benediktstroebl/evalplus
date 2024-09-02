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
    while paren_string:
        if not paren_string.startswith('('):
            raise ValueError('The given string is not valid, should start with "("')
        current_group = []
        while paren_string:
            current_group.append(paren_string[0])
            paren_string = paren_string[1:]
            if not paren_string:
                raise ValueError('The given string is not valid, should end with ")".')
            if current_group[-1] == '(':
                current_group.extend(separate_paren_groups(paren_string))
            elif current_group[-1] == ')':
                groups.append(''.join(current_group[:-1]))
                break
    return groups
