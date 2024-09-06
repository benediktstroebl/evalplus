from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    result: List[str] = []
    curr_group: str = ''
    depth: int = 0
    for char in paren_string:
        if char == '(':
            depth += 1
            curr_group += char
        elif char == ')':
            depth -= 1
            curr_group += char
            if depth == 0:
                result.append(curr_group)
                curr_group = ''
    return result
