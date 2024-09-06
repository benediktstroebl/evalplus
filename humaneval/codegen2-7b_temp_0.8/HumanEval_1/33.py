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

    open_paren_count = 0
    last_open_paren_location = 0
    for current_location, char in enumerate(paren_string):
        if char == '(':
            open_paren_count += 1
            if open_paren_count == 1:
                groups.append(paren_string[last_open_paren_location:current_location])
                last_open_paren_location = current_location
        elif char == ')':
            open_paren_count -= 1

    groups.append(paren_string[last_open_paren_location:])

    
