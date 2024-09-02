from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """BEGIN PSEUDOCODE"""
    # init a list
    # init a count variable
    # init a counter variable
    # iterate over the string
    # if the character is an open brace
    #   if count is 0
    #     append an empty string to the list
    #     increment the count
    #   add one to the counter
    # else if the character is a closing brace
    #   decrement the counter
    #   if count is 0
    #     increment the count
    # append the character to the list at the index of the counter
    # return the list
    pass

