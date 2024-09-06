from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # If the string is empty, return an empty list
    if len(paren_string) == 0:
        return []
    # Start off with an empty list
    separated_paren_groups = []
    # Check if the first brace is an opening brace
    if paren_string[0] == '(':
        # If it is, recursively call the function on the string minus the first character
        separated_paren_groups.append(separate_paren_groups(paren_string[1:]))
    # If the first brace is not an opening brace, check if it is a closing brace
    elif paren_string[0] == ')':
        # If it is, throw a ValueError
        raise ValueError("Input string is not a balanced group")
    else:
        # If it is not a closing brace or an opening brace, check if there is an opening brace after it
        if '(' in paren_string[1:]:
            # If there is, recursively call the function on the string minus the first character
            separated_paren_groups.append(separate_paren_groups(paren_string[1:]))
        # If there isn't, check if there is a closing brace after it
        elif ')' in paren_string[1:]:
            # If there is, throw a ValueError
            raise ValueError("Input string is not a balanced group")
        else:
            # If there isn't, append the first character to the list
            separated_paren_groups.append(paren_string[0])
    return separated_paren_groups

