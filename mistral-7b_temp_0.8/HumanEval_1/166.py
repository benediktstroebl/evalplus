from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_list = []
    current_paren = ""
    for char in paren_string:
        if char == "(":
            current_paren += char
        elif char == ")":
            if len(current_paren) == 0:
                raise ValueError("Opening paren not found")
            else:
                paren_list.append(current_paren)
                current_paren = ""
        else:
            raise ValueError("Not expecting this character")
    if len(current_paren) != 0:
        raise ValueError("Closing paren not found")
    return paren_list

