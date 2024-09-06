from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    open_count = 0
    list_groups = []
    curr_group = ""
    for ch in paren_string:
        if ch == '(':
            open_count += 1
            curr_group += ch
        elif ch == ')':
            open_count -= 1
            curr_group += ch
            if open_count == 0:
                list_groups.append(curr_group)
                curr_group = ""
        else:
            continue
    return list_groups

