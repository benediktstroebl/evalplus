from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    ans = []

    lst = list(paren_string)
    start = 0
    while start < len(lst):
        if lst[start] == '(':
            while start < len(lst) and lst[start] != ')':
                start += 1
            ans.append(''.join(lst[start + 1: start]))
            start += 1
        else:
            start += 1
    return ans

