from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if '(' not in paren_string or ')' not in paren_string:
        return [paren_string]

    parens_stack = []
    result = []

    for i, c in enumerate(paren_string):
        if c == '(':
            parens_stack.append(i)
        if c == ')':
            paren_start = parens_stack.pop()
            result.append(paren_string[paren_start:i + 1])

    return result

