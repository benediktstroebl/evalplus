from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Initialize an empty list to store the results
    results = []

    # Use a stack to keep track of the opening and closing parentheses
    stack = [('', '')]
    for i, char in enumerate(paren_string):
        # If we have a right parenthesis
        if char == ')':
            # If the stack is empty or the current character is not a left parenthesis
            if not stack or char != '(':
                # Push the current character onto the stack
                stack.append(char)
            # If the top of the stack is a right parenthesis, it's a group
            if ')' in stack:
                # Find the corresponding left parenthesis
                j = stack.index('(', stack.index(')') + 1)
                # Get the group of parentheses and remove it from the stack
                group = paren_string[j:i+1]
                stack.pop(stack.index(')', j))
                results.append(group)
                # Reset the stack
                stack = [('', '')]
        # If we have a left parenthesis
        elif char == '(':
            # If the stack is not empty, it's a nested group
            if stack:
                # Push the current character onto the stack
                stack[-1] = char
            # Otherwise, it's the start of a new group
            else:
                # Push the current character onto the stack
                stack.append(char)

    # If the stack is not empty, it's a nested group
    if stack:
        # Push the current character onto the stack
        stack[-1] = char
    # Otherwise, it's the end of the string
    else:
        pass

    # Remove the left parenthesis that is not paired with a right parenthesis
    for i, char in enumerate(paren_string):
        if char == '(':
            if paren_string[i+1] != ')':
                results.append('')

    return results

