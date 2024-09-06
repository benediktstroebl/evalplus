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
    current_str = ''

    for c in paren_string:
        if c == ')':
            if current_str[0] == '(':
                current_str = current_str[1:]
            else:
                if current_str:
                    result.append(current_str)
                current_str = ''
        else:
            current_str += c

    if current_str:
        result.append(current_str)

    return result

