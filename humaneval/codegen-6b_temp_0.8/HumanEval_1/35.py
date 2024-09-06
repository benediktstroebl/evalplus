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
    result = []
    for paren in paren_string:
        if paren == ')':
            if not paren_stack:
                raise IndexError('Too many closing ")"')
            paren_stack.pop()
        elif paren == '(':
            paren_stack.append('(')
        elif paren == '}':
            if not paren_stack:
                raise IndexError('Too many closing "}"')
            paren_stack.pop()
        elif paren == '{':
            paren_stack.append('{')
        # Ignore spaces
        elif paren == ' ':
            continue
        else:
            result.append(paren)
    if paren_stack:
        raise IndexError('Not balanced')
    return result

