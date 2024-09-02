from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_braces = []
    for index, char in enumerate(paren_string):
        if char == '(':
            open_braces.append(index)
        elif char == ')':
            if len(open_braces) == 0:
                return 'Error'
            open_braces.pop()
    if len(open_braces) != 0:
        return 'Error'
    else:
        output = []
        for index, char in enumerate(paren_string):
            if char == '(':
                output.append(paren_string[index:])
        return output

