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
    current_group = ''
    for i, char in enumerate(paren_string):
        if char == '(':
            current_group += char
        elif char == ')':
            if current_group == '':
                current_group = char
            elif current_group[-1] == '(':
                current_group += char
            else:
                current_group = current_group[:-1] + char
                paren_groups.append(current_group)
                current_group = ''
    paren_groups.append(current_group)
    return paren_groups

