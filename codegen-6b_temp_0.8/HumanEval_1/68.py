from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if len(paren_string) == 0:
        return []

    paren_stack = []
    open_count = 0
    paren_stack.append(paren_string[0])
    for c in paren_string[1:]:
        if c == '(':
            paren_stack.append('(')
            open_count += 1
        elif c == ')':
            if open_count > 0:
                paren_stack.append(')')
                open_count -= 1
            else:
                break
        elif c == '(':
            paren_stack.append('(')
            open_count += 1
    if open_count != 0:
        return separate_paren_groups(paren_string[open_count:])
    else:
        return [''.join(paren_stack)]

