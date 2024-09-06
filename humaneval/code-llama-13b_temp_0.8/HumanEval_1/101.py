from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    left = 0
    right = len(paren_string) - 1
    lists = []
    while right > left:
        i = left
        j = right
        while i < j:
            if paren_string[i] == '(' and paren_string[j] == ')':
                lists.append(paren_string[i:j + 1])
                left = j + 1
                right = len(paren_string) - 1
                break
            else:
                i += 1
                j -= 1
    return lists

