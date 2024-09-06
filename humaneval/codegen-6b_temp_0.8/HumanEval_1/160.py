from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    
    # loop through each char in string, if char is open paren, push to stack
    # if char is close parenthesis, pop from stack and write to stack
    # once stack is empty, append strings to list
    # if we reach the end of string, we can safely return the list
    
    stack = []
    result = []
    
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0:
                return result
            else:
                result.append(stack.pop())
    
    result.append(stack.pop())
    
    return result
        
    
