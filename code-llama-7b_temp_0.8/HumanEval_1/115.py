from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    # initialize the stack and the start index of a new group
    stack = []
    new_group_start = 0
    # iterate over the input string's characters
    for idx, char in enumerate(paren_string):
        # if the character is an opening bracket, start a new group and push it onto the stack
        if char == "(":
            stack.append(idx)
            new_group_start = idx
        # if the character is a closing bracket, pop the stack and check if it matches the current index
        elif char == ")":
            if not stack:
                raise ValueError("unbalanced parentheses")
            stack.pop()
            # if it's a match, append the string to the result
            if stack[-1] == new_group_start:
                result.append(paren_string[new_group_start : idx + 1])
    # if the stack is empty at the end, we have successfully separated all the groups
    if stack:
        raise ValueError("unbalanced parentheses")
    return result

