from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    open_parens = ['(', '[']
    close_parens = [')', ']']
    result = []

    stack = []
    for char in paren_string:
        if char in open_parens:
            stack.append(char)
        elif char in close_parens:
            if not stack or stack.pop()!= close_parens[open_parens.index(char)]:
                return result
            else:
                result.append(stack)
                stack = []
    return
