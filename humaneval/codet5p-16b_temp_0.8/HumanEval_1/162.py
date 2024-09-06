from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string = paren_string.replace(' ', '')
    stack = []
    output = []
    paren_index = 0
    while paren_index < len(paren_string):
        char = paren_string[paren_index]
        if char == '(':
            stack.append('(')
        elif char == ')':
            if not stack:
                raise ValueError(f'Invalid parentheses string, {paren_string}')
            top = stack.pop()
            if top!= '(':
                raise ValueError(f'Invalid parentheses string, {paren_string}')
            output.append(''.join(stack))
            stack = []
        else:
            raise ValueError(f'Invalid parentheses string, {paren_string}')
        paren_index += 1
    output.append(''.join(stack))
    return output
