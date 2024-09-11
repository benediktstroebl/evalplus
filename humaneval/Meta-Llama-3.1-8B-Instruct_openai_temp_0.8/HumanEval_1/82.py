```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty string to store the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # Add the closing parenthesis to the current group
            current_group += char
            # Add the current group to the result list
            result.append(current_group)
            # Reset the current group
            current_group = ""
    
    # Return the result list
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each containing a separate group of nested parentheses. It removes spaces from the input string, iterates over each character, and adds characters to the current group. When a closing parenthesis is encountered, the current group is added to the result list and reset. Finally, the script tests the function with the provided example.