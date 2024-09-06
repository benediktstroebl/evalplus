from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # find the first opening brace
    # we want to check if the opening brace is
    # not a part of some larger group
    i = 0
    while i < len(paren_string) and paren_string[i] != '(':
        i += 1
    if i == len(paren_string):
        return []
    # find the corresponding closing brace
    j = i + 1
    while j < len(paren_string) and paren_string[j] != ')':
        j += 1
    if j == len(paren_string):
        return []
    # check if the closing brace closes the group
    while j < len(paren_string) and paren_string[j] == paren_string[i]:
        i += 1
        j += 1
    if i != j:
        return []
    # check if the group is nested within a larger group
    # if it is, there are no balanced groups to return
    while i > 0 and paren_string[i - 1] == paren_string[j]:
        i
