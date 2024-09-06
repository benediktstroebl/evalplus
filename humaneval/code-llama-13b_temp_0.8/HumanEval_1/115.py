from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_bracket_count = 0
    current_string = ''
    res = []
    for char in paren_string:
        if char == '(':
            open_bracket_count += 1
            current_string += char
        elif char == ')':
            open_bracket_count -= 1
            if open_bracket_count == 0:
                res.append(current_string)
                current_string = ''
            else:
                current_string += char
    return res

