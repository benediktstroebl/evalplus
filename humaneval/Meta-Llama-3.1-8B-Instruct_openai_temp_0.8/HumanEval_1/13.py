```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    def count_open_paren(open_parenthesis: str) -> int:
        """
        This function counts the number of open parentheses in the input string.

        Args:
        open_parenthesis (str): A string of nested parentheses.

        Returns:
        int: The number of open parentheses in the input string.
        """
        return open_parenthesis.count('(')

    def count_close_paren(close_parenthesis: str) -> int:
        """
        This function counts the number of close parentheses in the input string.

        Args:
        close_parenthesis (str): A string of nested parentheses.

        Returns:
        int: The number of close parentheses in the input string.
        """
        return close_parenthesis.count(')')

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize the start index to 0
    start_index = 0

    # Iterate over the string to find separate groups
    while start_index < len(paren_string):
        # Initialize a counter for the number of open and close parentheses
        open_paren_count = 0
        close_paren_count = 0

        # Initialize the end index to the current start index
        end_index = start_index

        # Iterate over the string to count the number of open and close parentheses
        for i in range(start_index, len(paren_string)):
            # If an open parenthesis is found, increment the counter
            if paren_string[i] == '(':
                open_paren_count += 1
            # If a close parenthesis is found, increment the counter
            elif paren_string[i] == ')':
                close_paren_count += 1

            # If the number of open and close parentheses is equal, update the end index
            if open_paren_count == close_paren_count:
                end_index = i
                break

        # If the number of open and close parentheses is equal, it means we have found a separate group
        if open_paren_count == close_paren_count:
            # Extract the separate group from the string and add it to the list
            separate_groups.append(paren_string[start_index:end_index+1])
            # Update the start index to the end index + 1
            start_index = end_index + 1
        else:
            # If we have not found a separate group, increment the start index by 1
            start_index += 1

    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script first defines a helper function to count the number of open and close parentheses in a string. It then iterates over the input string to find separate groups of nested parentheses. When a separate group is found, it extracts the group from the string and adds it to the list of separate groups. The script finally returns the list of separate groups.