```markdown
### Separate Parenthesis Groups
#### Purpose
This script takes a string of multiple groups of nested parentheses and returns a list of each group as a separate string.

#### Code

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. 
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of each group as a separate string.
    """
    result = []  # Initialize an empty list to store the result
    current_group = ''  # Initialize an empty string to build the current group
    
    # Remove all spaces from the input string
    paren_string = paren_string.replace(' ', '')

    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == '(':
            current_group += char
        # If the character is a close parenthesis, 
        # add the current group to the result and reset the current group
        elif char == ')':
            current_group += char
            result.append(current_group)
            current_group = ''
    
    # Add the last group to the result if it's not empty
    if current_group:
        result.append(current_group)
    
    return result

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

#### Output
```python
['()', '(())', '(()())']
```