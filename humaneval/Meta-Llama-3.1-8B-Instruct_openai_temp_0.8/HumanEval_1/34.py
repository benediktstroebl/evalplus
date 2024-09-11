### Separate Paren Groups

```python
from typing import List
import stack

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate paren groups as strings.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store separated groups
    groups = []
    
    # Initialize an empty stack to keep track of parentheses
    paren_stack = stack.Stack()

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            paren_stack.push(char)
            current_group += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is empty or the top of the stack is not an opening parenthesis
            if not paren_stack:
                return []
            else:
                top = paren_stack.pop()
                # If the stack is empty after popping, it means we have a separate group
                if not paren_stack:
                    groups.append(current_group)
                    current_group = ""
                # If we have a separate group and it's not empty
                elif current_group:
                    groups.append(current_group)
                    current_group = top + current_group
                # If we're still building the current group
                else:
                    current_group = top + current_group

    # If there's a remaining group in the current_group, add it to the list
    if current_group:
        groups.append(current_group)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # ['()', '(())', '(()())']
```

This code defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate paren groups. It uses a stack to keep track of the parentheses and a list to store the separated groups. The function iterates over the input string, adding parentheses to the current group and popping them from the stack when it encounters a closing parenthesis. When the stack is empty, it means we have a separate group, which is added to the list. At the end, any remaining group in the `current_group` is added to the list.