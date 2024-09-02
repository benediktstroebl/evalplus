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
    for p in paren_string:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                result.append('')
            else:
                popped = stack.pop()
                if p == popped:
                    result.append('')
                else:
                    result[-1] += popped
    return result

