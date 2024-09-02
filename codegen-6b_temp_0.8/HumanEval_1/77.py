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
    paren_string = paren_string.replace(' ', '')
    for c in paren_string:
        if c == '(':
            paren_stack.append(c)
        elif c == ')':
            found = last_index_of(paren_stack, '(')
            if found is not None:
                paren_stack.pop(found)
            else:
                return None
    if len(paren_stack) == 0:
        return ['']
    return None

