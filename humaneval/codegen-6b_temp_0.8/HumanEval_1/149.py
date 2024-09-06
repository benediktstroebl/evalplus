from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    # First, iterate through the string with a stack to keep track of the balance of both braces
    stack_of_open_brace = []
    stack_of_close_brace = []
    
    open_brace = "("
    close_brace = ")"
    
    new_string = ""  # Initialize the new string
    
    for item in paren_string:
        if item == open_brace:
            stack_of_open_brace.append(item)
        elif item == close_brace:
            # There are two different cases:
            # 1. The stack is empty
            # 2. The current item is the second closing brace in the current set of opening parentheses
            # Check how balanced the braces are:
            if not stack_of_open_brace:
                # A) Balance 1: the second closing brace is outside the set of opening braces
                # B) Balance 2: the second closing brace is inside the set of opening braces
                # Error
                raise Exception("Unbalanced: ( ) (( ))")
            elif stack_of_open_brace[-1] == open_brace:
                # Case 1: The stack is empty
                new_string += item
            elif stack_of_open_brace[-1] == close_brace:
                # Case 2: the second closing brace is inside the set of opening braces
                # Remove the first element from the stack
                stack_of_open_brace.pop()
                # Append the current closing brace
                new_string += item
            else:
                # Case 3: the second closing brace is outside the set of opening braces
                # We may not have a balanced set of braces
                # Error
                raise Exception("Unbalanced: ( ) (( ))")

    if stack_of_open_brace:
        # There are still some braces left open
        raise Exception("Unbalanced: ( ) (( ))")

    return [new_string]

