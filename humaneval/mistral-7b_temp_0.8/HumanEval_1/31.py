from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if paren_string == '':
        return []

    count_left_paren = 0
    count_right_paren = 0
    stack = []
    result = []
    for i, char in enumerate(paren_string):
        if char == '(':
            count_left_paren += 1
        if char == ')':
            count_right_paren += 1

        if count_left_paren == count_right_paren:
            stack.append(''.join(paren_string[0:i + 1]))
            result.append(''.join(paren_string[0:i + 1]))
            count_left_paren = 0
            count_right_paren = 0

        if i == len(paren_string) - 1:
            stack.append(''.join(paren_string[0:i + 1]))
            result.append(''.join(paren_string[0:i + 1]))

    return result
