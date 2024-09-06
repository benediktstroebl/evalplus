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
    result = []
    for index, char in enumerate(paren_string):
        if char == '(':
            stack.append((index, char))
        elif char == ')':
            if len(stack) == 0:
                raise ValueError('Invalid input string')
            last_index, last_char = stack.pop()
            if last_char == '(':
                result.append(paren_string[last_index: index + 1])
    if len(stack)!= 0:
        raise ValueError('Invalid input string')
    return result

