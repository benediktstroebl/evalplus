from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    pass
    result = []
    current_paren_group = []
    for char in paren_string:
        if char == '(':
            current_paren_group.append(char)
        elif char == ')':
            if current_paren_group[-1] == '(':
                current_paren_group.pop()
                current_paren_group.append(char)
            else:
                result.append(''.join(current_paren_group))
                current_paren_group = []
    return result

