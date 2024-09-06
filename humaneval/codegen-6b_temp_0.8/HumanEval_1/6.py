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
    paren_index = 0
    separate_groups = []
    while paren_index < len(paren_string):
        if paren_string[paren_index] == '(':
            paren_stack.append(paren_index)
        elif paren_string[paren_index] == ')':
            if len(paren_stack) > 0:
                paren_index = paren_stack.pop()
            else:
                break
        else:
            pass
        paren_index += 1

    while len(paren_stack) > 0:
        separate_groups.append(paren_string[paren_stack.pop():paren_index])

    return separate_groups

