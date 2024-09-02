from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []
    open_paren_count = 0
    close_paren_count = 0
    result = []
    for char in paren_string:
        if char == '(':
            open_paren_count += 1
        elif char == ')':
            close_paren_count += 1
        if open_paren_count == close_paren_count:
            result.append(paren_string[:open_paren_count + close_paren_count])
            paren_string = paren_string[open_paren_count + close_paren_count:]
            open_paren_count = 0
            close_paren_count = 0
    if open_paren_count != close_paren_count:
        raise Exception("Open and close paren count is not equal")
    return result

