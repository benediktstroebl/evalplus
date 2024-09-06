from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    ret = []
    last_op = False
    for i in range(len(paren_string)):
        # check if the current paren is open or closed
        if paren_string[i] == '(':
            # if the last paren was closed, this is the start of a new group
            last_op = True
        elif paren_string[i] == ')':
            # if the last paren was open, this is the end of a group
            last_op = False
        # handle nested groups
        elif last_op and paren_string[i] == '(':
            ret.append(paren_string[i])
            last_op = True
        else:
            ret.append(paren_string[i])
    return ret

