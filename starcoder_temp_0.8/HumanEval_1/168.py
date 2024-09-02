from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []

    i = 0
    j = 0
    stack = []

    while j < len(paren_string):
        if paren_string[j] == '(':
            stack.append('(')
            j += 1

        elif paren_string[j] == ')':
            stack.pop()
            j += 1

        else:
            j += 1

        if len(stack) == 0:
            result.append(paren_string[i:j])
            i = j

    return result

