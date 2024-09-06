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
    if not paren_string:
        return []
    while len(paren_string) > 0:
        curr_group = ''
        for paren in paren_string:
            if paren == '(' or paren == ')':
                curr_group += paren
            elif curr_group!= '' and (paren == '(' or paren == ')'):
                paren_groups.append(curr_group)
                curr_group = ''
        paren_string = paren_string[len(curr_group):]
    return paren_groups
    
