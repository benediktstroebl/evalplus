from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_stack = []
    paren_string = paren_string.replace(" ", "")
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            paren_stack.append(paren_string[i])
        else:
            if len(paren_stack) > 0:
                paren_stack.pop()
    separated_paren_groups = [paren_string[:i] for i in range(len(paren_string), 0, -1) if len(paren_stack) == 0]
    return separated_paren_groups

