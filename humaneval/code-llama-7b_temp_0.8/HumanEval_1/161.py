from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    output = []
    curr_str = ''
    paren_balance = 0
    for c in paren_string:
        if c == '(':
            paren_balance += 1
        elif c == ')':
            paren_balance -= 1
        if c != ')' and paren_balance == 0:
            output.append(curr_str)
            curr_str = ''
        elif c != '(' and c != ')':
            curr_str += c
    return output

