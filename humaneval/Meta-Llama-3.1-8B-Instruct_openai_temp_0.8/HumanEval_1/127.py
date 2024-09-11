```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates balanced groups of nested parentheses from a given string into a list.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings where each string represents a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # If the current group is not empty (i.e., we have found the end of a group)
            if current_group:
                # Add the current group to the list of groups
                groups.append(current_group + char)
                # Reset the current group
                current_group = ""
            # If the current group is empty (i.e., the last character was the start of a group and we're finding the end)
            else:
                # Add the current character to the current group
                current_group += char
    
    # If the input string ends with an open parenthesis, add the current group to the list of groups
    if current_group:
        groups.append(current_group)
    
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This Python script defines a function `separate_paren_groups` that takes a string of balanced parentheses as input, removes any spaces, and separates the groups into a list of strings. The function iterates over each character in the input string, building the current group of parentheses and adding it to the list when a close parenthesis is found. If the input string ends with an open parenthesis, the current group is added to the list. The function is tested with the example provided in the problem statement.