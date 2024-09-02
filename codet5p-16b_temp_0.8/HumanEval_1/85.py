from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separated_groups = []

    open_paren_stack = []

    for character in paren_string:
        if character == '(':
            open_paren_stack.append(character)
        else:
            if len(open_paren_stack) > 0:
                open_paren_stack.pop()
            else:
                separated_groups.append(''.join(open_paren_stack))
                open_paren_stack = []

    if len(open_paren_stack) > 0:
        separated_groups.append(''.join(open_paren_stack))

    return separated_groups

