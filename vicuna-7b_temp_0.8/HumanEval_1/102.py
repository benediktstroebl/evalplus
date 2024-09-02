from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return_list = []
    last_open_brace = None
    last_close_brace = None
    for char in paren_string:
        if char == '(':
            if last_open_brace is not None and last_open_brace != ')':
                last_close_brace.append(last_open_brace)
                last_open_brace = None
            last_open_brace = char
        elif char == ')':
            if last_close_brace is not None and last_close_brace != '(':
                last_close_brace.append(last_open_brace)
                last_open_brace = None
            last_close_brace = char
        elif last_open_brace is not None and last_close_brace is not None and last_open_brace != last_close_brace:
            return_list.append(last_open_brace)
            last_open_brace = None
            last_close_brace = None
    if last_open_brace is not None and last_close_brace is not None and last_open_brace != last_close_brace:
        return_list.append(last_open_brace)
    return return_list
