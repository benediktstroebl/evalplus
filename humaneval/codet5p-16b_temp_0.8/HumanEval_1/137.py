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
    separated_groups = []
    for character in paren_string:
        if character == '(':
            stack.append(character)
        elif character == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        else:
            separated_groups.append(''.join(stack))
            stack = []
    return separated_groups

