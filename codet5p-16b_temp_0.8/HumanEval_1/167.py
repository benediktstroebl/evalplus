from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_string_list = list(paren_string)
    open_parenthesis = []
    res = []
    for index, char in enumerate(paren_string_list):
        if char == '(':
            open_parenthesis.append(index)
        if char == ')':
            close_parenthesis = open_parenthesis.pop()
            res.append(paren_string_list[open_parenthesis[-1] + 1: close_parenthesis])
            open_parenthesis.append(index)
    res.append(paren_string_list[open_parenthesis[-1] + 1:])
    return res

