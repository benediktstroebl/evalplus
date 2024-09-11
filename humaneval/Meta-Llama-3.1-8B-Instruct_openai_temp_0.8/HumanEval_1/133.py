```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.
    
    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of separate strings, each containing a group of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the result
    result = []
    
    # Initialize an empty stack to store the index of opening parentheses
    stack = []
    
    # Initialize the start index of the current group
    start = 0
    
    # Iterate over the string
    for i, char in enumerate(paren_string):
        if char == '(':
            # If it's an opening parenthesis, store its index in the stack
            stack.append(i)
        elif char == ')':
            # If it's a closing parenthesis, pop the index of the corresponding opening parenthesis from the stack
            stack.pop()
            # If the stack is empty, it means we've found a complete group
            if not stack:
                # Add the current group to the result
                result.append(paren_string[start:i+1])
                # Update the start index for the next group
                start = i + 1
    
    # Return the list of separate groups
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of separate groups. It uses a stack to keep track of the indices of opening parentheses and iterates over the string to find complete groups.