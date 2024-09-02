from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    stack: List[List[str]] = []
    result: List[str] = []
    for i, c in enumerate(paren_string):
        if c == '(':
            stack.append([])
        elif c == ')':
            if len(stack) > 0:
                stack.pop()
            else:
                result.append('()')
                continue
        elif c == ' ':
            continue
        stack[-1].append(c)
    if len(stack) == 0:
        return result
    current_string = stack.pop()
    while len(stack) > 0:
        current_string = current_string + stack.pop()
    result.append(''.join(current_string))
    return result

