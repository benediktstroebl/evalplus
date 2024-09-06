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

    for c in paren_string:
        if c == '(' or c == '{':
            paren_stack.append(c)
        elif c == ')' or c == '}':
            check = paren_stack.pop()
            if check is '(':
                result.append('')
            elif check is '{':
                result.append('{}')
            elif check is ')':
                result.append('')
            else:
                result.append('{')

    return result

