```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    Parameters:
    paren_string (str): The input string containing multiple groups of nested parentheses.
    
    Returns:
    List[str]: A list of strings, where each string is a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Initialize an empty list to store the separate groups
    groups = []
    
    # Initialize an empty string to build the current group
    current_group = ""
    
    # Initialize a counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == "(":
            balance += 1
            # If the balance is 1, it means we've started a new group, so add the current group to the list
            if balance == 1:
                groups.append(current_group)
                current_group = ""
        # If the character is a close parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            # Add the close parenthesis to the current group
            current_group += char
        # If the character is not a parenthesis, add it to the current group
        else:
            current_group += char
    
    # Add the last group to the list
    groups.append(current_group)
    
    # Return the list of separate groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to separate the groups of parentheses. It keeps track of the balance of parentheses using a counter and adds the current group to the list whenever a new group is started. The last group is added after the loop. The function first removes spaces from the input string and then iterates over each character in the string, adding it to the current group or starting a new group as necessary.