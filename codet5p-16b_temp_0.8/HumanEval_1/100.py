from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    if paren_string.count('(')!= paren_string.count(')'):
        return []
    if len(paren_string) == 0:
        return []
    stack = []
    current_group = ''
    for c in paren_string:
        if c == '(' and current_group == '':
            current_group = c
            stack.append(current_group)
        elif c == ')':
            current_group += c
            stack.pop()
            if current_group!= '':
                current_group = ''
        else:
            current_group += c
    if current_group!= '':
        stack.append(current_group)
    return stack
