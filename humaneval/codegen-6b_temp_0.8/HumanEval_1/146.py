from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output: List[str] = []
    paren_stack: List[str] = []
    i = 0
    while i < len(paren_string):
        c = paren_string[i]
        if c == '(':
            paren_stack.append(c)
        elif c == ')':
            if len(paren_stack) == 0:
                output.append(paren_string[0:i])
                paren_stack.pop()
            elif paren_stack[-1] == '(':
                paren_stack.pop()
            else:
                paren_stack.append(paren_string[i])
        elif c == ' ':
            pass
        else:
            paren_stack.append(paren_string[i])
        i += 1
    if len(paren_stack) > 0:
        output.append(''.join(paren_stack))
    return output

