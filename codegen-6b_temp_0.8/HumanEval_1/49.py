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
    for c in paren_string:
        if c == '(':
            paren_stack.append(c)
        elif c == ')':
            if len(paren_stack) == 0:
                return []
            top = paren_stack.pop()
        elif c == ' ':
            continue
        else:
            if len(paren_stack) == 0:
                paren_stack.append(c)
            elif paren_stack[-1] == '(':
                return []

    if len(paren_stack) > 0:
        return []

    return_strings = []
    N = len(paren_string)
    i = 0
    start = -1
    while i < N:
        if paren_stack:
            if paren_stack[-1] == '(':
                if i == start:
                    return_strings.append(paren_string[start:i])
                    start = -1
                    continue
                else:
                    start = i
            paren_stack.pop()
        if start < 0:
            return_strings.append(paren_string[i])
        i += 1
    if start >= 0:
        return_strings.append(paren_string[start:])
    return return_strings

