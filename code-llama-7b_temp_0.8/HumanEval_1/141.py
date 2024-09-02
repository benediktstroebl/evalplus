from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    """BEGIN PSEUDOCODE"""
    # This problem can be broken down into the following steps:
    # 1. Get the number of opening braces and closing braces in the string. 
    # 2. Initialize two variables: starting_position and ending_position
    # 3. Use a for loop to iterate through the length of the string
    # 4. Increment the ending_position value if you come across a closing brace
    # 5. Increment the starting_position value if you come across an opening brace
    # 6. Append the substring between the starting and ending position to the list
    # 7. Return the list
    # """
    """ END PSEUDOCODE """

    # first get the length of the input string
    length_of_string = len(paren_string)

    # Initialize the two variables
    starting_position = 0
    ending_position = 0

    # Initialize a list to hold the results
    list_of_paren_groups = []

    # Initialize the counter to zero
    counter = 0

    # iterate through the length of the string and compare the characters in the string
    for i in range(length_of_string):
        # Increment the counter if you come across a closing brace
        if paren_string[i] == ')':
            counter += 1

        # Increment the ending position if you come across an opening brace
        if paren_string[i] == '(':
            ending_position += 1

        # Append the substring between the starting and ending position to the list
        if paren_string[i] == ')':
            if counter == ending_position:
                list_of_paren_groups.append(paren_string[starting_position:ending_position + 1])
                counter = 0
                starting_position = ending_position + 1
                ending_position = starting_position

    # Return the list
    return list_of_paren_groups

