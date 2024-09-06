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
    in_balanced_group = False
    group = ''
    for char in paren_string:
        if char == '(':
            if not in_balanced_group:
                in_balanced_group = True
                group += char
            else:
                group += char
        elif char == ')':
            if in_balanced_group:
                group += char
                in_balanced_group = False
                res.append(group)
                group = ''
    return res

