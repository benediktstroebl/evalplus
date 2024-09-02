from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    braces = {'(': ')', '{': '}', '[': ']', '<': '>'}
    stack = []
    output = []
    for c in paren_string:
        if c in braces:
            stack.append(braces[c])
        elif not stack or braces[stack[-1]]!= c:
            continue
        else:
            stack.pop()
    return [s for s in stack[::-1]
