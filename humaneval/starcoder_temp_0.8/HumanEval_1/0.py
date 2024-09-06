from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # I'll use a stack to store the opening parenthesis
    # Whenever I encounter an opening parenthesis, I will push it onto the stack
    # If I encounter a closing parenthesis, I will pop the last element from the stack
    # If the last element on the stack is an opening parenthesis, then we have a match
    # If the last element on the stack is a closing parenthesis, then we don't have a match
    # If the last element on the stack is not a parenthesis, then it must have been a closing parenthesis.
    # In this case, we are guaranteed to encounter a closing parenthesis. We will pop it off the stack
    # and add the string from the opening parenthesis to the string from the closing parenthesis
    # We then re-append the popped closing parenthesis to the string from the opening parenthesis.
    # This is the new closing parenthesis, and we append it to the list of strings
    # We then do this until we have a stack with one element. That's the answer.
    # Here is how the above example works:
    # '' -> Stack -> []
    # '(' -> Stack -> ['(']
    # ')' -> Stack -> []
    # '(' -> Stack -> ['(', '(']
    # ')' -> Stack -> ['(']
    # '(' -> Stack -> ['(', '(']
    # ')' -> Stack -> ['(', '(', '(', ')', ')']
    # '(' -> Stack -> ['(', '(', '(', '(', '(']
    # ')' -> Stack -> ['(', '(', '(', '(']
    # ')' -> Stack -> ['(', '(', '(']
    # ')' -> Stack -> ['(', '(']
    # ')' -> Stack -> ['(']
    # Stack -> ['(']
    # ['(']
    stack = []
    output = []
    for c in paren_string:
        if c == '(':
            stack.append(c)
        elif c == ')':
            # We have to have something on the stack to pop
            # If there is something on the stack, then we can try to close the parentheses
            if stack:
                # Pop the last element off the stack
                top = stack.pop()
                # If the top of the stack is a '(' then we have a match.
                if top == '(':
                    # The output is the string between the last opening and the current closing parenthesis
                    # If the stack is empty, then the output is just the closing
