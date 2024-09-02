from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    out_list = []
    for paren_group in paren_string:
        if paren_group == '(':
            out_list.append(paren_group)
        elif paren_group == ')':
            if out_list[-1] == '(':
                out_list.pop()
            else:
                out_list.append(paren_group)
    return out
