from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    current = paren_string
    while current:
        open_count = 0
        for c in current:
            if c == '(':
                open_count += 1
            elif c == ')':
                open_count -= 1
        if open_count == 0:
            stack.append(current)
            current = ''
        else:
            current = current[open_count:]
    return stack

