from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    opening_brace_count = 0
    closing_brace_count = 0
    for char in paren_string:
        if char == '(':
            opening_brace_count += 1
        elif char == ')':
            closing_brace_count += 1
            if opening_brace_count - closing_brace_count < 0:
                raise ValueError("The input is not balanced")
        elif char == ' ':
            pass
    return [paren_string[i:i + 2] for i in range(0, len(paren_string), 2)]
