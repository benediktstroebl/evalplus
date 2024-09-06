from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []
    # print(f"paren_string = '{paren_string}'")
    left_paren_idx = paren_string.find('(')
    if left_paren_idx < 0:
        return []
    right_paren_idx = paren_string.find(')', left_paren_idx + 1)
    if right_paren_idx < 0:
        return []
    # print(f"left_paren_idx = {left_paren_idx}, right_paren_idx = {right_paren_idx}")
    return [paren_string[left_paren_idx:right_paren_idx + 1]] + \
           separate_paren_groups(paren_string[right_paren_idx + 1:])

