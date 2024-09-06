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
    stack = []
    output = []
    for char in paren_string:
        if char in ('(', '{', '['):
            stack.append(char)
        elif char in (')', '}', ']'):
            if len(stack) == 0 or stack[-1]!= '[':
                return []
            else:
                stack.pop()
        else:
            stack.append(char)
    while len(stack):
        output.append(stack.pop())
    return
