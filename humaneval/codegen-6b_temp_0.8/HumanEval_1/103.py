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
    result = []
    last = 0
    if not paren_string:
        return []
    for i, p in enumerate(paren_string):
        if p == '(':
            stack.append(i)
        elif p == ')':
            if stack:
                stack.pop()
                result.append(paren_string[last:i + 1])
                last = i + 1
            else:
                result.append(paren_string[last:i + 1])
                last = i + 1
    result.append(paren_string[last:])
    return result

