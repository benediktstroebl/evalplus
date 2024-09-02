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

    paren_string = paren_string.replace(' ', '')

    paren_string_list: List[str] = []
    current_string: List[str] = []

    for index, char in enumerate(paren_string):
        if char == '(':
            current_string.append('(')
        elif char == ')':
            current_string.append(')')
            if len(current_string) == 1:
                paren_string_list.append(''.join(current_string))
                current_string.clear()
    return paren_string_list

