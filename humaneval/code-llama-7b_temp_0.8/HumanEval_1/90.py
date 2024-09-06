from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # if input is empty
    if not paren_string:
        return []

    # Initialize a stack and list of strings
    stack = []
    paren_list = []

    # Loop through each character of input string
    for char in paren_string:
        if char in "([":
            stack.append(char)
        elif char in ")]":
            stack.append(char)
        else:
            continue

        # Whenever we hit the end of input string, and if stack is empty
        # it means we found a complete group
        if not stack:
            paren_list.append("".join(stack))
            stack = []

    # If there are still brackets in stack then we have an unbalanced paren string
    if stack:
        raise ValueError("Parentheses are unbalanced")

    return paren_list

