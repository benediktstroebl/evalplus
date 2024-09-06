from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    if not paren_string:
        return result
    stack = []
    for char in paren_string:
        if char == '(':
            stack.append('(')
        elif char == ')':
            if stack:
                stack.pop()
            else:
                stack.append(')')

    if stack:
        raise ValueError(f"Parentheses are not balanced for string '{paren_string}'")

    result = []
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            while paren_string[i] != ')':
                i += 1
            result.append(paren_string[i + 1:i + 1 + (paren_string.index('(', i + 1) - i - 1)])
            i += (paren_string.index('(', i + 1) - i - 1)
        else:
            i += 1
    return result

