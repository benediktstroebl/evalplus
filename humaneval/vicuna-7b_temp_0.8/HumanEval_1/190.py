from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create a dictionary to keep track of the open and closed parentheses.
    # The number of keys in the dictionary will be equal to the number of groups in the input string
    # If a key in the dictionary is ')' or '}' it will be set to False so that we can check if the
    # current group is balanced.
    # If a key is '(' it will be set to True so that we can check if the next character is a ')'.
    open_closed = {'}': False, '(': True}

    # Create an empty list to store the result
    result = []

    # Iterate over the characters in the input string, using a nested loop to iterate over the nested groups
    for char1, char2 in zip(paren_string, paren_string[1:]):
        # If the first character is a left parenthesis, add it to the result list and set the open_closed dictionary
        # to indicate that the current group is unbalanced
        if char1 == '(':
            result.append(char1)
            open_closed['('] = False
        # If the last character is a right parenthesis, and the open_closed dictionary indicates that the
        # current group is unbalanced, add the ')' to the result list and set the open_closed dictionary
        # to indicate that the current group is balanced
        elif char2 == ')' and open_closed['(']:
            result.append(char2)
            open_closed[')'] = True
        # If the first and last character are the same, and the open_closed dictionary indicates that the
        # current group is unbalanced, add the ')' to the result list and set the open_closed dictionary
        # to indicate that the current group is balanced
        elif char1 == char2 and open_closed['(']:
            result.append(char1)
            open_closed[')'] = True

    return result