from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # separate_paren_groups('( ) (( )) (( )( ))')
    # [
    #   '()',
    #   '(())',
    #   '(()())'
    # ]
    # return

    if len(paren_string) == 0:
        return []

    stack = []
    groups = []
    open_parens = 0
    for char in paren_string:
        if char == '(':
            open_parens += 1
        elif char == ')':
            if open_parens == 0:
                raise ValueError('Invalid input string')
            open_parens -= 1
            if open_parens == 0:
                groups.append(''.join(stack))
                stack.clear()
        else:
            stack.append(char)
    if open_parens!= 0:
        raise ValueError('Invalid input string')
    return groups

