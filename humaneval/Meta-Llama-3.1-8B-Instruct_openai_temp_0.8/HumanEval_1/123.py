```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into individual strings.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string represents a separate group of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Use a stack to keep track of the current group
    stack = []

    # Initialize a flag to indicate whether we're currently inside a group
    inside_group = False

    # Initialize a string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If we encounter an open parenthesis, add it to the current group and push it onto the stack
        if char == "(":
            current_group += char
            stack.append(char)
            inside_group = True

        # If we encounter a close parenthesis, pop the corresponding open parenthesis from the stack
        elif char == ")":
            current_group += char
            stack.pop()
            inside_group = False

        # If we're not inside a group, add the current character to the separate_groups list
        if not inside_group:
            if current_group:
                separate_groups.append(current_group)
                current_group = ""
            separate_groups.append(char)

    # Add any remaining characters to the separate_groups list
    if current_group:
        separate_groups.append(current_group)

    # Initialize an empty list to store the final result
    result = []

    # Iterate over each group in the separate_groups list
    for group in separate_groups:
        # If the group is not a single parenthesis, add it to the result list
        if group.count("(")!= group.count(")"):
            result.append(group)

    # Return the result list
    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that separates groups of nested parentheses in a given string into individual strings. It uses a stack to keep track of the current group and handles the input string iteratively. The function handles single parentheses as well, so the output will only contain groups that are not single parentheses.