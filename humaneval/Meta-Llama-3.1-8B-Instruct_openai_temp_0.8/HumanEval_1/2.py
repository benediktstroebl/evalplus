```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and returns a list of separate groups.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separate groups of nested parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Initialize an empty list to store the separate groups
    separate_groups = []
    
    # Initialize a counter to keep track of the current group
    group_counter = 0
    
    # Initialize an empty string to build the current group
    current_group = ''
    
    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group and increment the group counter
        if char == '(':
            current_group += char
            group_counter += 1
        # If the character is a close parenthesis, add it to the current group and decrement the group counter
        elif char == ')':
            current_group += char
            group_counter -= 1
            # If the group counter is zero, it means we've found a complete group, so add it to the list and reset the current group and group counter
            if group_counter == 0:
                separate_groups.append(current_group)
                current_group = ''
                group_counter = 0
    
    # Return the list of separate groups
    return separate_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( *))'))
```

Note: I have also added a test case at the end to demonstrate the function's behavior. The test case is modified to include a `*` character, which should be ignored. If you want to ignore any character that is not a parenthesis, you can modify the if-elif block to check for `char not in '()'.