from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Hint: don't write any code before this comment
    # Your implementation code here
    paren_list = []
    current = ''
    opened = 0
    for i in paren_string:
        if i == '(':
            opened += 1
            current += i
        elif i == ')':
            opened -= 1
            current += i
        elif i == ' ':
            continue
        else:
            raise Exception('Invalid input')
        if opened == 0:
            paren_list.append(current)
            current = ''
    return paren_list
