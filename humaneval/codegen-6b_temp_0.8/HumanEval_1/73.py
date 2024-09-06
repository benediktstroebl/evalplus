from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_braces = []
    result = []
    for char in paren_string:
        if char == "(":
            open_braces.append(char)
        elif char == ")":
            prev_brace = open_braces.pop()
            result.append(char * calc_nested_paren_size(open_braces))
        else:
            result.append(char)
    return result

