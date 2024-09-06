from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Base Cases
    if len(paren_string) == 0:
        return []
    if paren_string[0] != '(':
        return [paren_string[0]] + separate_paren_groups(paren_string[1:])
    if paren_string[-1] != ')':
        return separate_paren_groups(paren_string[1:])

    # Inductive Steps
    start_index = 0
    end_index = 1
    # Find first index of ')'
    while paren_string[end_index] != ')':
        end_index += 1
    return separate_paren_groups(paren_string[end_index + 1:]) + [paren_string[start_index:end_index + 1]]

