from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    parens = []
    for char in paren_string:
        if char == "(" or char == ")":
            stack.append(char)
        elif char == " ":
            continue
        else:
            if not stack:
                parens.append(char)
            else:
                char_remove = stack.pop()
                parens.append(char_remove + char)
    return parens
