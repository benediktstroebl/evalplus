from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result, count, current_string = [], 0, ''
    for ch in paren_string:
        if ch == '(':
            count += 1
            current_string += ch
        elif count > 0:
            current_string += ch
            if ch == ')':
                count -= 1
            if count == 0:
                result.append(current_string)
                current_string = ''
    return result

