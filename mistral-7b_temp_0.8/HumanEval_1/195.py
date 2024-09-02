from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # check if the paren string is empty
    if not paren_string:
        return []

    # create a list to store the separated paren groups
    separated_paren_groups = []

    # initialize a counter to track the number of open and close parentheses
    open_paren_count = 0
    close_paren_count = 0

    # iterate over the paren string
    for char in paren_string:

        # if the current character is an open parenthesis, increment the open parenthesis counter
        if char == '(':
            open_paren_count += 1

        # if the current character is a close parenthesis, increment the close parenthesis counter
        elif char == ')':
            close_paren_count += 1

        # if the number of open parentheses is equal to the number of close parentheses,
        # we have a balanced group of parentheses
        if open_paren_count == close_paren_count:

            # extract the balanced group of parentheses and add it to the list of separated paren groups
           
