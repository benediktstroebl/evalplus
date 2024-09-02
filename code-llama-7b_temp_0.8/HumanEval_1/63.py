from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    current_group_start = 0
    group_count = 0
    grouped_strings = []
    for i in range(1, len(paren_string) - 1):
        if paren_string[i] == '(':
            group_count += 1
        elif paren_string[i] == ')':
            group_count -= 1
        elif paren_string[i] == ' ' and group_count == 0:
            grouped_strings.append(paren_string[current_group_start:i])
            current_group_start = i + 1
            group_count = 0
    if group_count == 0:
        grouped_strings.append(paren_string[current_group_start:])
    return grouped_strings

