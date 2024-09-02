from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Let's create a dictionary to keep track of the nesting of the parentheses
    nesting = {}
    for char in paren_string:
        if char == '(':
            nesting['level'] += 1
        elif char == ')':
            nesting['level'] -= 1
            if nesting['level'] < 0:
                nesting['level'] = 0
    # Create an empty list to store the results
    results = []
    # Iterate through the characters in the string
    for i, char in enumerate(paren_string):
        # If the current character is a left parenthesis, we have found a new group
        if char == '(':
            # If the nesting level is zero, we have found an opening brace of the current group
            if not nesting:
                # Add the current character to the results list
                results.append(paren_string[i:i+1])
            # If the nesting level is greater than zero, we are closing the brace of the previous group
            else:
                # Add the current character to the results list
                results.append(paren_string[i:i+1])
                # Remove the last element from the nesting dictionary (it is the closing brace of the previous group)
                del nesting[nesting['level']]
        # If the current character is a right parenthesis, we are closing the brace of the current group
        elif char == ')':
            # If the nesting level is zero, we have found a closing brace of the current group
            if not nesting:
                # Add the current character to the results list
                results.append(paren_string[i:i+1])
            # If the nesting level is greater than zero, we are closing the brace of the previous group
            else:
                # Add the current character to the results list
                results.append(paren_string[i:i+1])
                # If the closing brace is the last element in the nesting dictionary, we have reached the end of the input
                if nesting.get