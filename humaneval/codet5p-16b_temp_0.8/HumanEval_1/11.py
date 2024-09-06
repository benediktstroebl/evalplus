from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    res = []
    string_res = ''
    open_par = 0
    close_par = 0
    for character in paren_string:
        if character == '(':
            open_par += 1
            close_par = 0
        elif character == ')':
            close_par += 1
            open_par = 0

        if open_par > close_par:
            if string_res:
                res.append(string_res)
            string_res = ''
        else:
            string_res += character
    if string_res:
        res.append(string_res)
    return res

