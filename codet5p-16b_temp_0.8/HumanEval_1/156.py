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
    left_parens_in_curr_group = 0
    curr_group = ''

    for c in paren_string:
        if c == '(':
            left_parens_in_curr_group += 1
            curr_group += c
        else:
            if left_parens_in_curr_group > 0:
                curr_group += c
                left_parens_in_curr_group -= 1
            else:
                paren_groups.append(curr_group)
                curr_group = ''

    if curr_group!= '':
        paren_groups.append(curr_group)

    return paren_groups

