from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initiate variables
    stack = []
    final_list = []
    # Loop through each character in string
    for i in paren_string:
        # If we encounter a close bracket
        if i == ")":
            # Pop off the first item on the stack
            stack.pop(0)
        # If we encounter an open bracket
        elif i == "(":
            # Add the string to the stack
            stack.append("")
        # If there are 0 items on the stack
        if len(stack) == 0:
            # Then we have found a complete group
            final_list.append(stack[0])
    return final_list

