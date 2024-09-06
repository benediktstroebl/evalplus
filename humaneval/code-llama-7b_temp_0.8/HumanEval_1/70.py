from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    opening_paren = ['(']
    closing_paren = [')']
    paren_stack = []
    paren_strings = []

    for char in paren_string:
        if char in opening_paren:
            paren_stack.append(char)
        elif char in closing_paren:
            if not paren_stack:
                return []
            elif (len(paren_stack) == 1 and
                    paren_stack[0] in opening_paren and
                    char in closing_paren):
                paren_strings.append(paren_stack[0] + char)
                paren_stack = paren_stack[:-1]
            else:
                paren_stack.append(char)
        else:
            continue

    return paren_strings

