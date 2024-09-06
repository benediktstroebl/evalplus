from typing import List
def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )( ))')
    ['()', '(())', '(()())']
    """
    result: List[str] = []
    stack = []
    nested_stack = []

    for char in paren_string:
        if char == '(':
            stack.append(char)
            nested_stack.append('(')
        elif char == ')':
            # If there is a match, pop from both stacks
            if not nested_stack or nested_stack.pop() != '(':
                stack.pop()
            else:
                result.append(')'.join(stack))
                stack = []
                nested_stack = []
        elif char == ' ':
            # ignore spaces
            continue
        else:
            # If not an opening bracket, it's part of the innermost expression
            nested_stack.append(char)
    # Handle the remaining open brackets
    result.append(')'.join(stack))
    return result
paren_string = '( ) (( )) (( )( ))'