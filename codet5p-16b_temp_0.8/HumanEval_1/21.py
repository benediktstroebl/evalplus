from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_brace = '('
    close_brace = ')'
    output = []
    current_string = ''
    i = 0
    while i < len(paren_string):
        if paren_string[i] == open_brace:
            current_string += paren_string[i]
            i += 1
            while i < len(paren_string) and paren_string[i] == open_brace:
                current_string += paren_string[i]
                i += 1
            if current_string:
                output.append(current_string)
            current_string = ''
        else:
            current_string += paren_string[i]
            i += 1
    if current_string:
        output.append(current_string)
    return output
