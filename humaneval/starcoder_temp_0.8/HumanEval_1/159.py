from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    output: List[str] = []

    open_paren = 0
    close_paren = 0
    start_pos = 0
    for index, char in enumerate(paren_string):
        if char == '(':
            open_paren += 1
        elif char == ')':
            close_paren += 1
        if open_paren == close_paren:
            output.append(paren_string[start_pos:index + 1])
            open_paren = 0
            close_paren = 0
            start_pos = index + 1
    return output

