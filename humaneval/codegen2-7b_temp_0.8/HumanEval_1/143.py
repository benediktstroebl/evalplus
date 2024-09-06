from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    group = ""
    paren_strings = []
    for c in paren_string:
        if c == "(":
            group += c
        elif c == ")":
            if group == "":
                continue
            paren_strings.append(group)
            group = ""
        else:
            group += c
    if group!= "":
        paren_strings.append(group)
    return paren_strings
