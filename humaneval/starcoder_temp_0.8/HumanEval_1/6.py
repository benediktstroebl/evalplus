from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    for char in paren_string:
        if char == "(":
            paren_groups.append([])
        elif char == ")":
            group_start = paren_groups.pop()
            paren_groups[-1] += group_start
        elif paren_groups:
            paren_groups[-1].append(char)
    return ["".join(group) for group in paren_groups]

