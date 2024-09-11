```markdown
### Separate Parentheses Groups
#### Problem Description
Input to this function is a string containing multiple groups of nested parentheses. 
Your goal is to separate those groups into separate strings and return the list of those.

#### Code Solution
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): Input string containing groups of nested parentheses.

    Returns:
    List[str]: List of separated groups of parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char
            # If the balance is zero, it means we have a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""
        
        # If the character is not a parenthesis, skip it

    # Return the list of separated groups
    return groups
```

#### Example Usage
```python
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
```
This script defines a function `separate_paren_groups` that separates groups of nested parentheses in a string into separate strings. It uses a balance counter to keep track of the parentheses in each group and builds the current group until it finds a matching close parenthesis. The function returns a list of the separated groups.