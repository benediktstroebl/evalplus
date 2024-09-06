from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = re.sub(r'\s', '', paren_string)
    paren_stack = []
    current_paren_group = ''
    for c in paren_string:
        if c == '(':
            paren_stack.append(current_paren_group)
            current_paren_group = ''
        elif c == ')':
            current_paren_group += c
        else:
            current_paren_group += c
    return paren_stack + [current_paren_group
