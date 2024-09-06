from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    level = 0
    paren_groups = []
    paren_string = paren_string.replace(" ", "")
    for i in range(len(paren_string)):
        if paren_string[i] == "(":
            level += 1
        elif paren_string[i] == ")":
            level -= 1
        if level == 0 and i < len(paren_string) - 1:
            paren_groups.append(paren_string[0 : i + 1])
            paren_string = paren_string[i + 1 :]
            i = -1
    return paren_groups

