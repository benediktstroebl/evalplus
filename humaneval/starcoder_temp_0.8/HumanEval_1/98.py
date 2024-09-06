from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Create a list to hold the individual paren groups
    paren_groups = []
    # Loop through each char in the paren_string
    for char in paren_string:
        # Check if the char is a left paren
        if char == '(':
            # Create a list to store chars for the current paren group
            paren_group = []
            # Append the char to the paren_group
            paren_group.append(char)
            # Increment the index by 1
            index += 1
        # Check if the char is a right paren
        elif char == ')':
            # Append the char to the paren_group
            paren_group.append(char)
            # Increment the index by 1
            index += 1
            # Check if the paren_group is balanced
            if len(paren_group) == 0 or paren_group[0]!= '(':
                # Throw an exception for an unbalanced paren_group
                raise Exception("Unbalanced Parentheses")
            # Otherwise, add the paren_group to the paren_groups list
            else:
                paren_groups.append(''.join(paren_group))
        # Add all other chars to the paren_group
        else:
            # Append the char to the paren_group
            paren_group.append(char)
    # Return the paren_groups
    return paren_groups
