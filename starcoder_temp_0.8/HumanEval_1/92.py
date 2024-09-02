from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # We'll use a stack to keep track of all the parenthesis that we've encountered
    stack = []
    # We'll use this to store the final list of strings
    group_list = []
    # Loop through the string
    for char in paren_string:
        # If the character is an open paren, add it to the stack
        if char == "(":
            stack.append(char)
        # If the character is a closed paren, pop the stack until you find the
        # corresponding open paren
        elif char == ")":
            # While the stack is not empty and the top of the stack is not an open paren
            while stack and stack[-1]!= "(":
                # Pop the stack into the final list
                group_list.append(stack.pop())
            # If the stack is empty, raise an error
            if not stack:
                raise ValueError(
                    "Unbalanced parentheses: no corresponding open paren to close"
                )
            # Otherwise, pop the open paren off the stack
            stack.pop()
    # If the stack is not empty, we have unbalanced parentheses, so raise an error
    if stack:
        raise ValueError("Unbalanced parentheses: unclosed groups")
    # Return the list of parentheses groups as a list of strings
    return group_list

