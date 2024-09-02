from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Create an empty list to store the results
    result_list = []

    # Initialize the current string to the empty string
    current_string = ""

    # Initialize the current group to an empty list
    current_group = []

    # Iterate through the string
    for char in paren_string:
        if char == "(":
            # If the current character is an open parenthesis, add it to the current group
            current_group.append(char)
        elif char == ")":
            # If the current character is a close parenthesis, check if the group is balanced
            if len(current_group) > 0 and current_group[-1] == "(":
                # If the group is balanced, remove the last parenthesis from the group and add the current string
                # to the result list
                current_group.pop()
                result_list.append(current_string)
                current_string = ""
            else:
                # If the group is not balanced, raise an exception
                raise Exception("Invalid parentheses")
        else:
