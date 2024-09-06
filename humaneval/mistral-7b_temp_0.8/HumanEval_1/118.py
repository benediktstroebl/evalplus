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
    result = []
    for s in paren_string:
        if s == '(':
            paren_stack.append(s)
        elif s == ')':
            if paren_stack:
                paren_stack.pop()
            else:
                result.append('')
        else:
            result[-1] += s

    result = [i for i in result if i]
    return result
