from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    level = 0
    current_paren_string = ""
    for paren in paren_string:
        if paren == "(":
            level += 1
        elif paren == ")":
            level -= 1
        if level == 0:
            result.append(current_paren_string)
            current_paren_string = ""
        else:
            current_paren_string += paren
    return result

