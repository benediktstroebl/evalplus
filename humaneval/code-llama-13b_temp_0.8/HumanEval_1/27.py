from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    open_bracket_indexes = []
    closed_bracket_indexes = []
    for i in range(len(paren_string)):
        if paren_string[i] == '(':
            open_bracket_indexes.append(i)
        elif paren_string[i] == ')':
            closed_bracket_indexes.append(i)
    groups = []
    for open_bracket_index, closed_bracket_index in zip(open_bracket_indexes, closed_bracket_indexes):
        groups.append(paren_string[open_bracket_index:closed_bracket_index+1])
    return groups

