from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    count = 0
    previous_index = 0
    for index, letter in enumerate(paren_string):
        if letter == '(':
            count += 1
        elif letter == ')':
            count -= 1
        if count == 0:
            result.append(paren_string[previous_index:index + 1])
            previous_index = index + 1
    return result

