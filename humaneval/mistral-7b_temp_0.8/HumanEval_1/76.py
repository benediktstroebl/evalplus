from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # input parsing
    if not paren_string:
        return []

    paren_string_no_spaces = ''.join(paren_string.split()).replace(' ', '')

    # we need to iterate over the strings in order to identify groups
    group_start_indices = [i for i, char in enumerate(paren_string_no_spaces) if char == '(']
    group_end_indices = [i for i, char in enumerate(paren_string_no_spaces) if char == ')']
    number_of_groups = len(group_start_indices)

    # we are going to store the balanced strings inside a list, so we are going to iterate over the groups starting
    # from the first
    for index in range(number_of_groups):
        # we are going to create a temporary string to store the current group
        # we start from the index of the current group and finish in the index of the next group
        balanced_string = paren_string_no_spaces[group_start_indices[index]:group_end_indices[
