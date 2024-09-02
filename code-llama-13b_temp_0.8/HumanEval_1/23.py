from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    res = []
    group = ""
    paren_count = 0
    for c in paren_string:
        if c == "(":
            paren_count += 1
        elif c == ")":
            paren_count -= 1
        if c == ")" and paren_count == 0:
            group += c
            res.append(group)
            group = ""
        else:
            group += c
    return res

