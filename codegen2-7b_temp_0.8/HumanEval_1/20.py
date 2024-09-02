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
    cur_paren_group = ''
    in_paren = False
    for char in paren_string:
        if char == '(':
            if in_paren:
                cur_paren_group += char
            else:
                paren_groups.append(cur_paren_group)
                cur_paren_group = ''
                in_paren = True
        else:
            cur_paren_group += char
            in_paren = False
    paren_groups.append(cur_paren_group)
    return paren_
