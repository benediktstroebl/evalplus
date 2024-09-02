from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []

    result_list = []
    current_str = ''

    for char in paren_string:
        if char in '()':
            current_str += char
        elif current_str:
            result_list.append(current_str)
            current_str = ''

    if current_str:
        result_list.append(current_str)

    return result_list

