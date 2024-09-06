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
            if not current_group:
                raise ValueError("Unbalanced group")
            current_group.pop()
        else:
            current_group.append(char)
        if not current_group:
            result.append(''.join(current_group))
    return
