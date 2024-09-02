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
    i = 0
    result = []
    while i < len(paren_string):
        char = paren_string[i]
        if char == '(':
            paren_stack.append(')')
        elif char == ')':
            while len(paren_stack) > 0 and paren_stack[-1] != '(':
                result.append(paren_stack.pop())
            if len(paren_stack) == 0:
                print("fail")
            paren_stack.pop()
        i += 1
    while len(paren_stack) > 0:
        result.append(paren_stack.pop())
    return result

