from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    current_group = []
    groups = []
    current_level = 0
    for index, character in enumerate(paren_string):
        if character == '(':
            current_level += 1
        elif character == ')':
            current_level -= 1
        if current_level == 0:
            if current_group:
                groups.append(''.join(current_group))
            current_group = [character]
        else:
            current_group.append(character)
    if current_group:
        groups.append(''.join(current_group))
    return groups

