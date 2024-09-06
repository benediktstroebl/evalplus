from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_parens = "("
    close_parens = ")"
    parens_stack = []
    open_parens_count = 0
    for char in paren_string:
        if char == open_parens:
            open_parens_count += 1
            parens_stack.append(char)
        elif char == close_parens:
            open_parens_count -= 1
            parens_stack.pop()
        else:
            pass
        if open_parens_count < 0:
            raise ValueError("Error: Parentheses are unbalanced")
    return [
        ''.join(parens_stack)
    ]
