from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Main idea:
    # we will use a stack, when we find an open bracket, we append it to the stack
    # when we find a close bracket, we pop the stack and add it to a result
    # until we find a closing bracket, we keep appending characters to the current string

    # 1. Base case:
    if not paren_string:
        return []

    # 2. Recursive step:
    # We will use a stack to keep track of the indices of the first open bracket of each group
    # so at any given moment we know the group it belongs to
    stack = []
    result = []
    current_group = ""
    for index, character in enumerate(paren_string):
        if character == "(":
            stack.append(index)
        elif character == ")":
            stack.pop()
            # once we find the closing bracket, we add that group to the result
            current_group += paren_string[stack[-1] + 1:index]
            result.append(current_group)
            current_group = ""
        # if the current character is neither "(" or ")", we append it to the current group
        else:
            current_group += character
    return result

