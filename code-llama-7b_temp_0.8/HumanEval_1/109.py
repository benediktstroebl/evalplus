from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Window is where we will be iterating through
    window: str = paren_string

    # keep_strings is our list of strings we will be returning
    keep_strings: List[str] = []

    # We will be iterating through the window looking for parenthesis.
    # The starting index for where we will search for parenthesis
    i: int = 0

    # We will be looping while there are parenthesis left in the window
    while '(' in window:

        # Find the index of the first parenthesis
        first_paren_index: int = window.find('(')
        # Find the index of the last parenthesis
        last_paren_index: int = window.find(')')

        # If the first parenthesis is before the last parenthesis
        # It means we have a valid group
        if first_paren_index < last_paren_index:
            # Then, let's extract the group, and add it to our keep strings
            keep_strings.append(window[first_paren_index:last_paren_index + 1])
            # Lastly, let's remove the group from our window, so that we
            # don't process it again
            window = window[last_paren_index + 1:]
        else:
            # If the first parenthesis is after the last parenthesis,
            # That means that we have an invalid group. We need to find the next valid group.
            i = find_next_valid_group(window, first_paren_index, i)
            # Once we find a valid group, we extract it from our window
            # and add it to our keep strings
            keep_strings.append(window[i:window.find('(', i + 1)])
            # Lastly, we find where the next parenthesis is, so that we can search for another group
            i = window.find('(', i + 1)

    # Return all the groups we found
    return keep_strings

