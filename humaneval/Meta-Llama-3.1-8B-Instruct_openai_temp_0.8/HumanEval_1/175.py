### Separate Paren Groups

The following Python script uses a stack to separate the groups of parentheses from a given input string.

```markdown
### Separate Paren Groups
#### Description
This script takes a string containing multiple groups of nested parentheses as input, separates these groups into individual strings, and returns a list of these strings.

#### Code
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from a string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize a stack to keep track of opening parentheses
    stack = []
    # Initialize a list to store the separated groups
    groups = []

    # Initialize a temporary string to build the current group
    temp = ""

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it onto the stack
        if char == "(":
            stack.append(char)
            temp += char
        # If the character is a closing parenthesis
        elif char == ")":
            # If the stack is not empty, pop the opening parenthesis from the stack
            if stack:
                stack.pop()
                temp += char
            # If the stack is empty, it means we've found a complete group
            else:
                # Add the complete group to the list
                groups.append(temp)
                temp = ""

    # Add any remaining group to the list
    if temp:
        groups.append(temp)

    return groups

### Example Usage
if __name__ == "__main__":
    # Test the function
    print(separate_paren_groups("( ) (( )) (( )( ))"))
    # Output: ['()', '(())', '(()())']
```

This script works by iterating over the input string and using a stack to keep track of opening parentheses. When it encounters a closing parenthesis, it checks if the stack is not empty, which means it's part of a group. If the stack is empty, it means the group is complete, so it adds the group to the list and resets the temporary string. Finally, it adds any remaining group to the list and returns the list of separated groups.