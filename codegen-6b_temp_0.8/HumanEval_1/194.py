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
    stack = []
    original = paren_string.strip()
    new = original.replace(' ', '')
    l = len(new)
    i = 0
    while (len(stack) > 0) or (i < l):
        if i < l and new[i] == '(':
            stack.append('(')
            i += 1
        elif i < l and new[i] == ')':
            stack.pop()
            i += 1
        if i < l and new[i] == '(':
            new = new[:i] + ')' + new[i + 1:]
            i += 1
        if len(stack) == 0:
            result.append(new)
            new = original.replace(' ', '')
            l = len(new)
            i = 0
    return result

