from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # initialize a list to hold the result
    result = []
    # return an empty list if there are no parentheses in the string
    if '(' not in paren_string and ')' not in paren_string:
        return result
    # remove any spaces in the string
    paren_string = paren_string.replace(' ', '')
    # a string to hold the current group of parentheses
    current_paren = ''
    # iterate through every character in the string
    for character in paren_string:
        # check if the character is an opening parenthesis
        if character == '(':
            # add the current group to the result
            result.append(current_paren)
            # reset the current group to an empty string
            current_paren = ''
        # check if the character is a closing parenthesis
        elif character == ')':
            # add the current group to the result
            result.append(current_paren)
            # reset the current group to an empty string
            current_paren = ''
        # add the character to the current group
        current_paren += character
    # append the last current group to the result
    result.append(current_paren)
    # return the result
    return result
