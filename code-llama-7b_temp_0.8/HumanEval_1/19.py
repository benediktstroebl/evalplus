from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Base Case: An empty string does not contain a parentheses group, return an empty list
    if not paren_string:
        return []

    # Divide the string by the opening parentheses.
    first_open_paren_index = paren_string.find('(')
    # Handle the case where the string does not contain an opening parentheses
    if first_open_paren_index == -1:
        return [paren_string]
    # Handle the case where the string contains only one parentheses group.
    elif first_open_paren_index == 0:
        return [paren_string]
    # Handle the case where the string contains two or more parentheses groups.
    else:
        # Get the index of the first closing parentheses that matches the first opening parentheses.
        first_close_paren_index = paren_string.find(')', first_open_paren_index)
        # Use slicing to obtain the first parentheses group.
        first_paren_group = paren_string[0:first_close_paren_index + 1]
        # Recursive call to obtain the rest of the string's parentheses groups.
        remaining_paren_groups = separate_paren_groups(paren_string[first_close_paren_index + 1:])
        # Put the parentheses groups together in a list.
        return [first_paren_group] + remaining_paren_groups

