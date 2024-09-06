from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_stack = []
    groups = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            paren_stack.append(paren_string[i])
        elif paren_string[i] == ')' and len(paren_stack) > 0:
            groups.append(paren_stack)
            paren_stack = []
        elif paren_string[i] == ')':
            return []
        i += 1

    if len(paren_stack) > 0:
        groups.append(paren_stack)
    return groups

