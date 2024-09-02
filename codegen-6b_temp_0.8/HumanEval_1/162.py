from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack = []
    parens = []
    i = 0
    while i < len(paren_string):
        c = paren_string[i]
        i += 1
        if c == '(':
            parens.append(c)
            stack.append(i)
            continue
        elif c == ')':
            if len(stack) == 0:
                parens.append(paren_string[i - 1])
                i += 1
                continue
            else:
                parens.append(paren_string[stack.pop() + 1:i])
    return parens

