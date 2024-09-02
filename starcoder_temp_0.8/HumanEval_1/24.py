from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    opening_chars = ['(', '[']
    closing_chars = [')', ']']

    paren_groups = []
    paren_stack = []

    for char in paren_string:

        if char in opening_chars:
            paren_stack.append(char)

        if char in closing_chars:
            pos = closing_chars.index(char)

            if (len(paren_stack) > 0) and (paren_stack[-1] == opening_chars[pos]):
                paren_stack.pop()
            else:
                paren_stack.append(char)

    if len(paren_stack) > 0:
        paren_groups.append(''.join(paren_stack))

    return paren_groups

