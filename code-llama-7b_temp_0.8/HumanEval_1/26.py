from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return_list = []

    # Return if paren_string is empty
    if not paren_string:
        return return_list

    # When we hit the end of the string, we can start another return_list.
    # Then start new open_paren_count and close_paren_count to zero.
    # Then move to the next index.
    # Also, we can break out of the while loop when the index is at the end of the string.

    # Set the first open_paren_count and close_paren_count
    open_paren_count = close_paren_count = 0

    # Init the index and the new_paren_string
    index = 0
    new_paren_string = ""

    # While loop that keeps going until the index is at the end of the string.
    while index < len(paren_string):

        # If we find an open paren, we can increment open_paren_count by 1.
        # If we find a close paren, we can increment close_paren_count by 1.

        # If the open_paren_count is zero and the close_paren_count is zero,
        # we can append the new_paren_string to the return_list and move on to the next index.

        # If the open_paren_count is greater than the close_paren_count, we can keep going.

        # If the open_paren_count is equal to the close_paren_count, we have a new paren_group.
        # We can append the new_paren_string to the return_list and reset the index.

        # And, if the open_paren_count is less than the close_paren_count,
        # we have a problem and we raise a ValueError.

        # If we don't find a paren, we can just continue through the string.
        if paren_string[index] == "(":
            open_paren_count += 1

        elif paren_string[index] == ")":
            close_paren_count += 1

        else:
           
