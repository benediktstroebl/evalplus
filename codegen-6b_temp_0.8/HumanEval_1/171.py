from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    if not paren_string:
        return []
    pos = 0
    paren_list = []
    while pos < len(paren_string):
        if paren_string[pos] == '(':
            paren_list.append(paren_string[pos:pos + 1])
        elif paren_string[pos] == ')':
            paren_list.append(paren_string[pos:pos + 1])
        pos += 1
    for i in range(len(paren_list)):
        paren_list[i] = paren_list[i][1:-1]
    return paren_list

