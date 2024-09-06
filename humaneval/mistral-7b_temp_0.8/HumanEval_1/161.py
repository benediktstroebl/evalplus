from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    l_stack = []
    stack = []
    for c in paren_string:
        if c == '(':
            l_stack.append(c)
        elif c == ')':
            if l_stack and l_stack[-1] == '(':
                l_stack.pop()
            else:
                stack.append(c)
    if l_stack:
        return []
    return stack[::-1]

