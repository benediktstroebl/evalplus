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
    open_braces = '({['
    close_braces = ')}]'
    open_braces_dict = {s: i for i, s in enumerate(open_braces)}
    close_braces_dict = {s: i for i, s in enumerate(close_braces)}
    open_stack = []
    ans = []
    for c in paren_string:
        if c in open_braces_dict:
            open_stack.append(open_braces_dict[c])
        elif c in close_braces_dict:
            if open_stack == []:
                print(f'Invalid string {paren_string}')
                return
            if close_braces_dict[c] == open_stack[-1]:
                open_stack.pop()
            else:
                print(f'Invalid string {paren_string}')
                return
    if open_stack:
        print(f'Invalid string {paren_string}')
        return
    for i, c
