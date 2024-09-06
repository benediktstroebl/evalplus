from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    start_paren = 0
    result_list = []
    # Keep track of how many sets of parentheses are open
    paren_stack = 0
    for i in range(len(paren_string)):
        # We are either at a closing parenthesis
        if paren_string[i] == ')':
            # Check that we have at least one open set of parentheses
            if paren_stack > 0:
                # Add the word between before the closing bracket and the
                # last opening bracket that was closed
                result_list.append(paren_string[start_paren:i])
                # Drop the number of open sets on the stack
                paren_stack -= 1
            # We are at a closing parenthesis
            start_paren = i + 1

    # Add the remaining open sets
    while paren_stack > 0:
        result_list.append(paren_string[start_paren:])
        # Drop the number of open sets on the stack
        paren_stack -= 1

    return result_list

