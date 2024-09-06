from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # use a stack to keep track of the parentheses
    # since they are nested, the first open parenthesis is the first to be popped
    # iterate through the string character by character
    # for each iteration, if we find an open parenthesis, push to stack
    # if we find a close parenthesis, pop from stack
    # if stack is empty, we have a seperate group
    # push seperate group to list
    # if stack is not empty, we have another group to consider

    # TODO
    # return the list

