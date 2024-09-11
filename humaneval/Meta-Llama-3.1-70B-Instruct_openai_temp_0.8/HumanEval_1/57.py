```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, 
    separates them into groups and returns a list of these groups.
    
    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings where each string is a separate group of parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to keep track of the nesting level
    nesting_level = 0
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increase the nesting level
        if char == "(":
            nesting_level += 1
        # If the character is a closing parenthesis, decrease the nesting level
        elif char == ")":
            nesting_level -= 1
        
        # Add the character to the current group
        current_group += char
        
        # If the nesting level is zero, it means we have a complete group
        if nesting_level == 0:
            # Add the current group to the result list
            result.append(current_group)
            # Reset the current group
            current_group = ""
    
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```