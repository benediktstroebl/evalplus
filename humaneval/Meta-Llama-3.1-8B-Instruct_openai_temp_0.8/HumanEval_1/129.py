Here's a Python script that implements a solution using a stack data structure to keep track of the opening parentheses and their indices.

```markdown
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of nested parentheses.

    """
    # Initialize an empty list to store the separated groups
    groups = []
    
    # Initialize an empty stack to keep track of opening parentheses and their indices
    stack = []
    
    # Initialize an empty string to build the current group
    curr_group = ""
    
    # Iterate over the input string
    for i, char in enumerate(paren_string):
        # If the character is an opening parenthesis, push it onto the stack along with its index
        if char == "(":
            stack.append((char, i))
            curr_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is empty, there's a mismatch, so ignore this group
            if not stack:
                continue
            # Pop the opening parenthesis from the stack along with its index
            _, open_idx = stack.pop()
            # Add the current group to the list of groups
            groups.append(paren_string[open_idx:i+1])
            # Reset the current group
            curr_group = ""
    
    # Return the list of separated groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a stack to keep track of opening parentheses and their indices. When a closing parenthesis is encountered, it checks if the stack is empty (which would indicate a mismatch) and if not, pops the corresponding opening parenthesis from the stack along with its index. The group of parentheses between these indices is then added to the list of groups. The current group is reset after each group is added to the list.