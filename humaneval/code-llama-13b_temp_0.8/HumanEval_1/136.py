from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    res = []
    temp = ''
    balance = 0
    for i in paren_string:
        if i == '(':
            balance += 1
            temp += i
        elif i == ')':
            balance -= 1
            if balance == 0:
                res.append(temp)
                temp = ''
            else:
                temp += i
    return res

