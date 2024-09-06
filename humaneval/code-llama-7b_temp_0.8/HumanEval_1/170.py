from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """BEGIN PSEUDOCODE"""
    # We know that we are always working with balanced parentheses.
    # We'll keep a stack of strings we're working on, and a stack of open parens we've seen.
    # For each character in the string:
    # If the character is an open paren, append it to the stack of open parens.
    # If the character is a close paren, pop an open paren off the stack and add it to the end of
    # the string we're working on.
    # When you hit the end of the string, return the stack of strings you're working on.
    """END PSEUDOCODE"""
    # CREATE VARIABLES
    # stack of strings we're working on
    stack: List[str] = []
    # stack of open parens we've seen
    paren_stack: List[str] = []

    # LOOP THROUGH EACH CHARACTER IN STRING
    for char in paren_string:
        # IF CHARACTER IS AN OPEN PAREN, PUSH ONE TO THE PAREN STACK
        if char == "(":
            paren_stack.append(char)
        # IF CHARACTER IS A CLOSE PAREN, POP OPEN PAREN OFF PAREN STACK AND ADD TO END OF STRING WE'RE WORKING ON
        elif char == ")":
            paren_stack.pop()
            stack.append(char)
        # IF CHARACTER IS A SPACE, IGNORE
        elif char == " ":
            pass
        # IF CHARACTER IS ANYTHING ELSE, ADD TO END OF STRING WE'RE WORKING ON
        else:
            stack.append(char)

    # RETURN STACK OF STRINGS WE'RE WORKING ON
    return stack

