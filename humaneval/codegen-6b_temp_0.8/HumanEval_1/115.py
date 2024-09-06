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
    results = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                raise ValueError('The input string is not valid')
            elif stack[-1] == '(':
                stack.pop()
            else:
                raise ValueError('Your input string is not valid')
    if len(stack) != 0:
        raise ValueError('The input string is not valid')

    for group in paren_string.split(' '):
        results.append(''.join(group))
    return results

