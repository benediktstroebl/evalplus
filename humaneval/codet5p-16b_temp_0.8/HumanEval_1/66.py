from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    paren_list = paren_string.split()
    paren_list = [i for i in paren_list if i!= '']
    open_paren_count = 0
    separated_groups = []
    for i in paren_list:
        if i == '(':
            open_paren_count += 1
        if i == ')':
            open_paren_count -= 1
        if open_paren_count == 0:
            separated_groups.append(i)
        if open_paren_count < 0:
            break
    return separated_groups
