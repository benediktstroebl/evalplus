from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    current_group = []
    for char in paren_string:
        if char == '(':
            current_group.append(char)
        elif char == ')':
            current_group.pop()
            if len(current_group) > 0:
                result.append(current_group)
                current_group = []
        elif char == ' ':
            # Ignore the spaces
            pass
        else:
            # If current_group is not empty, append to the result
            if len(current_group) > 0:
                result.append(current_group)
                current_group = []
    # If current_group is not empty, append to the result
    if len(current_group) > 0:
        result.append(current_group)
    return result

