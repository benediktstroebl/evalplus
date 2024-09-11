```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced nested parentheses from a string into a list of strings.

    Args:
    paren_string (str): Input string containing multiple groups of balanced nested parentheses.

    Returns:
    List[str]: List of separated groups of balanced nested parentheses.
    """
    paren_string = paren_string.replace(' ', '')  # Remove spaces
    groups = []  # Initialize an empty list to store the groups
    group = ''  # Initialize an empty string to build the current group
    depth = 0  # Initialize a counter to track the depth of parentheses

    for char in paren_string:
        if char == '(':  # If a left parenthesis is encountered, increase the depth
            group += char
            depth += 1
        elif char == ')':  # If a right parenthesis is encountered, decrease the depth
            group += char
            depth -= 1
            if depth == 0:  # If the depth becomes 0, it means we've found a complete group
                groups.append(group)  # Add the group to the list of groups
                group = ''  # Reset the current group
        else:  # If it's not a parenthesis, ignore it

    return groups  # Return the list of groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of balanced nested parentheses as input and returns a list of separated groups. The function iterates over the input string, keeping track of the depth of parentheses and building up groups of balanced parentheses. When a complete group is found, it is added to the list of groups and the current group is reset. The function returns the list of groups.