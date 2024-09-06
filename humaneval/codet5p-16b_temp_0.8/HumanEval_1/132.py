from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    separated = []
    current = ""
    paren_stack = []
    for i in paren_string:
        if i == "(":
            paren_stack.append(i)
            current += i
        elif i == ")":
            if len(paren_stack) == 0:
                raise Exception("Not balanced!")
            paren_stack.pop()
            current += i
        else:
            current += i
        if i == "(" and len(paren_stack) == 0:
            separated.append(current)
            current = ""
    if len(current) > 0:
        separated.append(current)
    return separated

