from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # create a list to store the separated groups
    groups = []
    
    # iterate through the input string
    for char in paren_string:
        # if the current character is an open brace, append it to the list and reset its state
        if char == '(':
            groups.append(char)
            char = ')'
        # if the current character is a close brace, check if the previous character is the same as the open brace
        # that was appended to the list, if so, append a string containing the open and close brace to the list
        # and reset the state of both the open and close brace
        elif char == ')':
            if groups[-1] == '(':
                groups.append('')
                char = '('
            else:
                groups.append('')
                groups.append(')')
                char = ')'
            groups.pop() # remove the open brace from the list
        # if the current character is neither an open nor a close brace, append it to the list
        else:
            groups.append(char)
    
    # return the list of separated groups
    return groups

