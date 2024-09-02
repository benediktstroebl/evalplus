from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Initialize the list that will contain the groups
    paren_groups = []

    # Calculate the total number of opening and closing parentheses
    number_open = paren_string.count('(')
    number_close = paren_string.count(')')

    # If there are more opening parentheses than closing parentheses, then there is an unmatched opening brace somewhere
    if number_open > number_close:
        raise Exception("There is an unmatched opening brace somewhere in the string")

    # Add to the list the string that begins at the 0th index and ends at the first close brace
    paren_groups.append(paren_string[0:paren_string.index(')') + 1])

    # Remove the substring from the start to the last close brace to the end
    paren_string = paren_string[paren_string.index(')') + 1:]

    # Call the function recursively until the paren string is empty
    return paren_groups + separate_paren_groups(paren_string)

