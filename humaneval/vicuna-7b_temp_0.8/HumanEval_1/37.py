from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create a list to store the final result
    result = []

    # Loop through each character in the input string
    for char in paren_string:
        # If the current character is an opening brace,
        # create a new group in the result list
        if char == '(':
            result.append('')
        # If the current character is a closing brace,
        # add it to the current group and move on to the next group
        elif char == ')':
            result[-1] += char
            del result[-1]
            result.append('')
        # If the current character is not a brace,
        # add it to the current group
        else:
            result[-1] += char

    # Add the last group to the result list
    result.append('')

    # Return the final result as a list of strings
    return result

