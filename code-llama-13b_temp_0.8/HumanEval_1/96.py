from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # solution
    open_indices = []
    out_list = []
    new_list = []
    for index, char in enumerate(paren_string):
        if char == '(':
            open_indices.append(index)
        if char == ')':
            start_index = open_indices.pop()
            out_list.append(paren_string[start_index: index + 1])
    return out_list

