from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    left_idx = paren_string.find('(')
    right_idx = paren_string.rfind(')')

    if left_idx == -1 or right_idx == -1:
        return []

    result = []

    while left_idx != -1 and right_idx != -1:
        result.append(paren_string[left_idx: right_idx + 1])
        paren_string = paren_string[:left_idx] + paren_string[right_idx + 1:]
        left_idx = paren_string.find('(')
        right_idx = paren_string.rfind(')')

    return result

