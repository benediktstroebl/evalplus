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
    group = ''
    count = 0
    for char in paren_string:
        if char == '(':
            count += 1
            group += char
        elif char == ')':
            count -= 1
            group += char
            if count == 0:
                groups.append(group)
                group = ''
        else:
            group += char
    return groups

