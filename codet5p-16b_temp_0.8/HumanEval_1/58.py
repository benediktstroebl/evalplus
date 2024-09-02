from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_groups = []
    curr_group = ''
    paren_stack = []
    for paren in paren_string:
        if paren == '(':
            paren_stack.append(paren)
            curr_group += paren
        else:
            if paren_stack:
                paren_stack.pop()
                curr_group += paren
            else:
                paren_groups.append(curr_group)
                curr_group = ''
                curr_group += paren
    paren_groups.append(curr_group)
    return paren_groups

