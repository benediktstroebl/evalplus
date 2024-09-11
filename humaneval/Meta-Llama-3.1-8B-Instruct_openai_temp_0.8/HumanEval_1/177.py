```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate strings, each containing a group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty stack to store the indices of opening parentheses
    stack = []
    # Initialize an empty list to store the results
    groups = []

    # Initialize an empty string to build the current group
    group = ""

    # Iterate over the characters in the input string
    for i, char in enumerate(paren_string):
        # If the character is an opening parenthesis, push its index onto the stack
        if char == "(":
            stack.append(i)
            # Add the character to the current group
            group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # Pop the index of the corresponding opening parenthesis from the stack
            opening_index = stack.pop()
            # Add the closing parenthesis to the current group
            group += char
            # Add the current group to the list of results
            groups.append(paren_string[opening_index:i+1])
            # Reset the current group
            group = ""

    # Return the list of groups
    return groups


# Test the function
if __name__ == "__main__":
    print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. The function uses a stack to keep track of the indices of opening parentheses and builds the current group of parentheses as it iterates over the input string. The function then resets the current group and adds it to the list of results when it encounters a closing parenthesis that corresponds to the top of the stack. Finally, the function returns the list of groups.

The script also includes a test case to demonstrate the function's behavior.