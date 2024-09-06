from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # break into groups
    paren_groups = []
    curr_paren_group = []
    index = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            curr_paren_group.append(index)
        elif paren_string[index] == ')':
            if curr_paren_group:
                curr_paren_group.pop()
        index += 1

    paren_groups.append(''.join([paren_string[i] for i in curr_paren_group]))
    index = 0
    while index < len(paren_string):
        if paren_string[index] == '(':
            curr_paren_group.append(index)
        elif paren_string[index] == ')':
            if curr_paren_group:
                curr_paren_group.pop()
        index += 1

    if curr_paren_group:
        paren_groups.append(''.join([paren_string[i] for i in curr_paren_group]))

    return paren_groups

