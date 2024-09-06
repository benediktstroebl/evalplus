from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_group = ""
    paren_group_list = []
    current_group = []
    for c in paren_string:
        if c == '(':
            current_group.append(c)
        elif c == ')':
            current_group.append(c)
            if not current_group[-1] == '(':
                paren_group = "".join(current_group)
                paren_group_list.append(paren_group)
                current_group = []
        else:
            pass
    if current_group:
        paren_group = "".join(current_group)
        paren_group_list.append(paren_group)

    return paren_group_list

