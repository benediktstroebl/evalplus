from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # initialize a stack
    stack = []
    result = []

    # loop through the string
    for char in paren_string:
        # if we see a left parenthesis, push it onto the stack
        if char == '(':
            stack.append(char)

        # if we see a right parenthesis, pop off the stack
        elif char == ')':
            # we pop off the stack until we find a left parenthesis
            while stack and stack[-1] != '(':
                stack.pop()
            # we pop off the left parenthesis too
            stack.pop()
            # if we make it here, we know we've got a valid group of parentheses
            if stack:
                # get the string representation of the group
                result.append(''.join(stack))
                # reset the stack
                stack = []

    return result

