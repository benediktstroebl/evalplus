```python
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates a given string of nested parentheses into individual groups of balanced parentheses.

    Args:
        paren_string (str): The input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, where each string is a group of balanced parentheses.
    """
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the input string
    groups = []  # Initialize an empty list to store the groups of parentheses

    while paren_string:  # Continue until the entire input string is processed
        open_count = 0  # Initialize a counter to keep track of the number of open parentheses
        for i in range(len(paren_string)):
            if paren_string[i] == "(":
                open_count += 1
            elif paren_string[i] == ")":
                open_count -= 1
            if open_count == 0:  # When the counter becomes zero, it means a balanced group is found
                groups.append(paren_string[:i+1])  # Append the found group to the list
                paren_string = paren_string[i+1:]  # Remove the found group from the input string
                break

    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of individual groups of balanced parentheses. It works by iterating through the input string, counting the number of open parentheses, and appending the found group to the list when the counter becomes zero. Finally, it returns the list of groups. The script also includes a test case to demonstrate the function's correctness.