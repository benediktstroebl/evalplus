from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.strip()
    if len(paren_string) == 0:
        return []
    groups = []
    group = ""
    open_paren = 0
    for char in paren_string:
        if char == ")":
            open_paren -= 1
        else:
            open_paren += 1
        group += char
        if open_paren == 0:
            groups.append(group)
            group = ""
    if len(group) > 0:
        groups.append(group)
    
