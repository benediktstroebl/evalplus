from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_paren_count = 0
    closed_paren_count = 0
    paren_groups = []
    temp_string = ""
    for char in paren_string:
        if char == "(":
            open_paren_count += 1
        elif char == ")":
            closed_paren_count += 1
            if closed_paren_count == open_paren_count:
                paren_groups.append(temp_string)
                temp_string = ""
                closed_paren_count = 0
                open_paren_count = 0
        temp_string += char
    return paren_groups

