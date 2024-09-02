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

    left_paren = 0
    right_paren = 0
    brackets = []
    for i in range(0, len(paren_string)):
        if paren_string[i] == '(':
            left_paren += 1
        if paren_string[i] == ')':
            right_paren += 1
        if left_paren == right_paren:
            brackets.append(paren_string[i])
    return brackets

