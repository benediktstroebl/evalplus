from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    list_of_parens = []
    open_brace_stack = []
    current_string = ''
    
    for char in paren_string:
        if char == '(':
            open_brace_stack.append(char)
        elif char == ')':
            if open_brace_stack:
                open_brace_stack.pop()
        else:
            current_string += char
            
        if not open_brace_stack:
            list_of_parens.append(current_string)
            current_string = ''
    
