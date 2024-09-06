from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    left = 0
    right = 0
    separated_groups = []
    while left < len(paren_string):
        if paren_string[left] == "(":
            left += 1
        else:
            right += 1
            if right == 0:
                separated_groups.append(paren_string[left:right])
        left = right
    return separated_
