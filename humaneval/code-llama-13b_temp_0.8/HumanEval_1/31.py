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
    new_str = ''
    paren_string = paren_string.replace(' ', '')
    for char in paren_string:
        if char == '(':
            stack.append(char)
            new_str += char
        elif char == ')':
            if stack.pop():
                new_str += char
        else:
            continue
    return [new_str[i:j] for i, j in zip([0] + [index + 1 for index, value in enumerate(new_str) if value == '('],
                                         [index for index, value in enumerate(new_str) if value == ')'] + [None])]
