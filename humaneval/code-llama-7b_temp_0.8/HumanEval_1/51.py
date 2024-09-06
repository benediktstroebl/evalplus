from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output_list: List[str] = []
    current_group: str = ''
    in_progress = False

    for character in paren_string:
        if character in ('(', '{'):
            in_progress = True
        elif character in (')', '}'):
            in_progress = False
            output_list.append(current_group)
            current_group = ''
        if in_progress:
            current_group += character

    return output_list

