Here is a Python script that contains a self-contained function that solves the problem of separating out parentheses from a given string:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Separate balanced parentheses from the string into separate strings.
    Parameters: String containing balanced parentheses
    Returns: List of strings, each representing a balanced parentheses group.
    """
    detailed_ docs: https://github.com/ Documents/python/docs/en/latest/auto-generated/ ))
    """
    # Create an empty list to store the output
    result = []

    # Iterate through each character in the string
    for char in parentheses:
        # If it's a closing parenthesis, add it to the result list
        if char == ')':
            result.append(')')
       
        # If it's an opening parenthesis, push it to the front of the stack
        elif char == '(':
            result.append(')')

    # Add the Strings until there are no more opening parentheses left
    return result
```
This code is designed to accept a string containing balanced parentheses and separate them into individual strings. It does this by iterating through each character in the string. After iterating through characters, the code checks if the character is a closing parenthesis (')') and appends it to the result string. If the character is an opening parenthesis ('), it is pushed into a stack. Then, once there are no more opening parentheses left, the function returns the result string.