from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_strings = []
    current_string = ""
    for char in paren_string:
        if char == "(":
            current_string += char
            continue
        if char == ")":
            paren_strings.append(current_string[1:-1])
            current_string = ""
            continue
        current_string += char
    paren_strings.append(current_string)
    return paren_strings

