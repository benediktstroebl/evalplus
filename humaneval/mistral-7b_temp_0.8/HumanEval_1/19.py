from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    s = paren_string.strip()
    left_par = 0
    right_par = 0
    parentheses_group = []

    for i in range(len(s)):
        if s[i] == '(':
            left_par += 1
        elif s[i] == ')':
            right_par += 1
        if left_par > right_par:
            return []

        if left_par == right_par:
            parentheses_group.append(s[:i + 1])
            left_par = 0
            right_par = 0
            s = s[i + 1:]

    return parentheses_group

