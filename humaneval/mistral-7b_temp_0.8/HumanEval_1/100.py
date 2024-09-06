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
    parentheses_list = []
    parentheses_string = ""
    for character in paren_string:
        if character == '(':
            parentheses_list.append(parentheses_string)
            parentheses_string = ""
        else:
            parentheses_string += character
    parentheses_list.append(parentheses_string)
    return parentheses_list
