from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    curr_string = ''
    i = 0
    paren_stack = []
    while i < len(paren_string):
        if paren_string[i] == '(':
            paren_stack.append(0)
            if paren_string[i + 1] == ')':
                curr_string += paren_string[i - len(curr_string) + 1:i + 2] + ' '
                i += 2
                curr_string = curr_string.strip()
            else:
                i += 1
        elif paren_string[i] == ')':
            if len(paren_stack) == 0:
                print('Illegal Parens')
                return
            paren_stack.pop()
            if len(paren_stack) == 0:
                curr_string += paren_string[i - len(curr_string) + 1:i + 1] + ' '
                i += 1
                curr_string = curr_string.strip()
        else:
            if len(paren_stack) == 0:
                curr_string += paren_string[i - len(curr_string) + 1:i + 1] + ' '
                i += 1
                curr_string = curr_string.strip()
    if len(curr_string) > 0:
        curr_string = curr_string.strip()
        paren_stack = []
    return curr_string.split()

