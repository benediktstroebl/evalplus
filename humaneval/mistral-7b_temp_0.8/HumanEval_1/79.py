from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Your code here
    open_braces_stack = []
    result = []
    for paren in paren_string:
        if paren == '(':
            open_braces_stack.append('(')
        elif paren == ')':
            open_braces_stack.pop()
            if len(open_braces_stack) == 0:
                result.append('')
            else:
                result[-1] += paren
    return result

