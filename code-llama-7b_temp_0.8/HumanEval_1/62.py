from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    parens = []
    counter = 0
    curr_string = ""
    for character in paren_string:
        if character == "(":
            counter += 1
        elif character == ")":
            counter -= 1
        if counter == 0 and len(curr_string) != 0:
            parens.append(curr_string)
            curr_string = ""
        else:
            curr_string += character
    if curr_string != "":
        parens.append(curr_string)
    return parens

