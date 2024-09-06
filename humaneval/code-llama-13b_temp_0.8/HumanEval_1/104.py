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

    output = []
    current_paren_string = ''
    prev_paren_idx = 0
    for i in range(len(paren_string)):
        current_char = paren_string[i]
        if current_char == '(':
            current_paren_string += current_char
        elif current_char == ')':
            current_paren_string += current_char
            output.append(current_paren_string)
            current_paren_string = ''
            prev_paren_idx = i
    return output

