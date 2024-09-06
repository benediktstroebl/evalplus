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
    current_string = ''
    open_count = 0
    for i in paren_string:
        if i == '(':
            open_count += 1
            current_string += i
        elif i == ')':
            open_count -= 1
            current_string += i
            if open_count == 0:
                result.append(current_string)
                current_string = ''
    return result

