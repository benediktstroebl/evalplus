```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of multiple groups of nested parentheses, 
    separates them into separate strings, and returns the list of those.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string represents a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of parentheses
    groups = []
    
    # Initialize an empty string to build the current group
    curr_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            curr_group += char
            
        # If the character is a close parenthesis
        elif char == ")":
            
            # Add the close parenthesis to the current group
            curr_group += char
            
            # If the current group is not empty, add it to the list of groups and reset the current group
            if curr_group:
                groups.append(curr_group)
                curr_group = ""
                
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings where each string represents a group of nested parentheses. The function works by iterating over the input string, building up each group of parentheses, and adding them to the list of groups when a close parenthesis is encountered. The function then returns the list of groups. The test case at the end of the script demonstrates the function's usage.