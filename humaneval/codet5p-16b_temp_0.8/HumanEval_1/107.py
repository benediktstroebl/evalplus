from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    left, right = 0, 0
    n = len(paren_string)
    result = []
    while left < n:
        if paren_string[left] == '(':
            right = left
            while right < n:
                if paren_string[right] == '(':
                    right += 1
                else:
                    break
            result.append(paren_string[left:right])
            left = right
        left += 1
    return result

