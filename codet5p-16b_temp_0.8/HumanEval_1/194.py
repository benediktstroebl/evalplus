from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    current_string: str = paren_string
    left_parenthesis = 0
    right_parenthesis = 0
    last_left = 0
    last_right = 0
    open_braces = 0
    closed_braces = 0
    list_paren = []

    for i in range(len(current_string)):
        if current_string[i] == '(':
            if left_parenthesis == right_parenthesis == 0 and open_braces == closed_braces == 0:
                last_left = i
            left_parenthesis += 1
        if current_string[i] == ')':
            right_parenthesis += 1
        if current_string[i] == '(':
            open_braces += 1
        if current_string[i] == ')':
            closed_braces += 1

    if left_parenthesis == right_parenthesis == 0 and open_braces == closed_braces == 0:
        last_right = i

    for i in range(last_left, last_right + 1):
        if current_string[i] == '(
