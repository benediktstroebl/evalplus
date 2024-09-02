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
    result = []
    # to separate group we will use position
    i = 0
    while i < len(paren_string):
        if paren_string[i] == '(':
            # find close paren
            close_paren = paren_string.find(')', i)
            # add the group
            result.append(paren_string[i: close_paren + 1])
            i = close_paren + 1
        else:
            i += 1
    return result

