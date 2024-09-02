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
    curr_string = ''
    last_index = -1
    for index, char in enumerate(paren_string):
        if char == '(':
            if last_index != -1:
                paren_groups.append(curr_string[last_index + 1: index])
            last_index = index
        elif char == ')':
            if index == len(paren_string) - 1:
                paren_groups.append(curr_string[last_index + 1:])
            else:
                paren_groups.append(curr_string[last_index + 1: index + 1])
            curr_string = ''
            last_index = -1
        elif last_index == -1:
            curr_string += char
    return paren_groups

