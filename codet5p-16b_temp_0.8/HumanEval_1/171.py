from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    list_of_parens = []
    open_braces_stack = []

    for char in paren_string:
        if char == "(":
            open_braces_stack.append(char)
        elif char == ")":
            open_braces_stack.pop()
        else:
            continue
        if open_braces_stack == []:
            list_of_parens.append("".join(open_braces_stack))
    return list_of_parens

