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
    open_braces = []
    for c in paren_string:
        if c == '(' or c == '{':
            open_braces.append(c)
        elif c == ')':
            current_string = current_string.strip()
            if len(current_string) > 0:
                result.append(current_string)
            current_string = ''
            if open_braces:
                open_braces.pop()
        elif c == '}':
            current_string = current_string.strip()
            if len(current_string) > 0:
                result.append(current_string)
            current_string = ''
            if open_braces:
                open_braces.pop()
    return result

