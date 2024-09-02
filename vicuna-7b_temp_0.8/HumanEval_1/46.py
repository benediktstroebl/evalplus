from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create an empty list to store the separated groups
    separated_groups = []
    
    # Use a nested loop to iterate over each character in the string
    for i, c in enumerate(paren_string):
        # If the current character is an opening parenthesis, add it to the list
        if c == '(':
            # Keep track of the opening and closing parenthesis count
            count = 1
            # Add the opening parenthesis to the list
            separated_groups.append('(')
        # If the current character is a closing parenthesis, add it to the list
        elif c == ')':
            # Decrement the opening and closing parenthesis count
            count = count - 1
            # If the count is zero, add the closing parenthesis to the list
            if count == 0:
                separated_groups.append(')')
        # If the current character is a space, ignore it
        elif c == ' ':
            pass
        # If the current character is a closing parenthesis that is not followed by an opening parenthesis,
        # add it to the list
        elif c == ')':
            if count == 0:
                separated_groups.append(')')
        # If the current character is not a valid opening or closing parenthesis, ignore it
        else:
            pass
    # Return the list of separated groups
    return separated_groups

