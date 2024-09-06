from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    new_string = ''
    stack = []
    for index in range(len(paren_string)):
        if paren_string[index] == '(':
            stack.append(index)
        elif paren_string[index] == ')':
            start_index = stack.pop()
            new_string += paren_string[start_index:index + 1]
    return new_string.split()

