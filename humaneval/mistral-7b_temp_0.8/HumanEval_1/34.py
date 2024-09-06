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
    for s in paren_string.split():
        if not s:
            continue
        braces = [0, 0]
        for c in s:
            if c == '(':
                braces[0] += 1
            elif c == ')':
                braces[0] -= 1
                braces[1] += 1
            if braces[0] < 0 or braces[0] > braces[1]:
                break
        else:
            result.append(s)
    return result
