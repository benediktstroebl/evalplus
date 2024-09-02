from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_braces = 0
    closed_braces = 0
    result = []
    temp_string = ''
    for i in paren_string:
        if i == '(':
            open_braces += 1
        elif i == ')':
            closed_braces += 1
        if open_braces == closed_braces:
            if i == '(':
                open_braces += 1
                temp_string += i
            elif i == ')':
                open_braces -= 1
                temp_string += i
                result.append(temp_string)
                temp_string = ''
    return result
