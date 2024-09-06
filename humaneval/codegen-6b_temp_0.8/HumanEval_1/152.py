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
    start_paren = None
    current_group = []
    for index, c in enumerate(paren_string):
        if c == '(':
            if start_paren is not None:
                current_group.append(c)
        elif c == ')':
            if start_paren is None:
                if current_group:
                    current_group.append(c)
            else:
                current_group.append(c)
                start_paren.extend(current_group)
                current_group = []
        elif c == ' ':
            if current_group:
                current_group.append(c)
        else:
            current_group.append(c)
        start_paren = c in '{'
    if current_group:
        paren_groups.append(''.join(current_group))
    return paren_groups

