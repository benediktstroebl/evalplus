from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separated_groups = []
    current_group = []
    for index, char in enumerate(paren_string):
        if char == '(':
            current_group.append(char)
        elif char == ')':
            current_group.pop()
            if len(current_group) == 0:
                separated_groups.append(paren_string[:index + 1])
                current_group = []
    return separated_groups

