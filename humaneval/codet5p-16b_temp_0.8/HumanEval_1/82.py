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

    output = []
    current_group = []
    balanced = False
    paren_string = paren_string.replace(' ', '')
    for i, char in enumerate(paren_string):
        if char == '(':
            if balanced:
                output.append(''.join(current_group))
                current_group = []
            current_group.append(char)
            balanced = False
        elif char == ')':
            if balanced:
                output.append(''.join(current_group))
                current_group = []
            current_group.append(char)
            balanced = True
        elif balanced:
            current_group.append(char)
        else:
            continue
    output.append(''.join(current_group))
    return output

