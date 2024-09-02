from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output = []
    stack = []
    for char in paren_string:
        if char == ')':
            substack = []
            while len(stack) != 0 and stack[-1] != '(':
                substack.append(stack.pop())
            stack.pop()
            stack.append(''.join(substack))
        elif char == '(':
            stack.append(char)
        elif char != ' ':
            stack.append(char)
    return stack

