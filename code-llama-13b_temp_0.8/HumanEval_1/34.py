from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    index = 0
    while index < len(paren_string):
        open_paren_index = paren_string.find('(', index)
        if open_paren_index == -1:
            break
        close_paren_index = paren_string.find(')', open_paren_index)
        while close_paren_index != -1 and paren_string[:close_paren_index].count('(') != paren_string[:close_paren_index].count(')'):
            close_paren_index = paren_string.find(')', close_paren_index+1)
        if close_paren_index != -1:
            groups.append(paren_string[open_paren_index:close_paren_index+1])
            index = close_paren_index + 1
        else:
            break
    return groups

