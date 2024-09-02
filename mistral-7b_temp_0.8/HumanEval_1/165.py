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
    group = []
    paren_string = list(paren_string)
    for paren in paren_string:
        if paren == '(':
            stack.append('(')
        elif paren == ')':
            if not stack:
                group.append(paren)
            elif stack[-1] == '(':
                stack.pop()
            else:
                group.append(paren)
    return ["".join(group)]

