from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_groups = []
    paren_stack = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            paren_stack.append(paren_string[i])
        elif paren_string[i] == ')':
            if len(paren_stack) == 0:
                break
            elif paren_stack[-1] == '(':
                paren_stack.pop()
            else:
                balance = len(paren_stack)
                paren_groups.append(paren_string[i - balance:i + 1])
                i -= balance
        i += 1
    return [paren_group.strip() for paren_group in paren_groups]

