### Parenthesis Group Separator
#### Problem Description
Separate groups of nested parentheses in a given string and return them as a list.

#### Solution
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a given string and return them as a list.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separated group of nested parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty stack to track the opening parentheses
    stack = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, push it to the stack
        if char == "(":
            stack.append(char)
            current_group += char
        # If the character is a closing parenthesis, pop the opening parenthesis from the stack
        elif char == ")":
            if stack:
                stack.pop()
                current_group += char
                # If the stack is empty after popping, it means we've found a complete group
                if not stack:
                    # Add the current group to the list of separated groups
                    separated_groups.append(current_group)
                    current_group = ""
            else:
                # If the stack is empty, it means there's a mismatched closing parenthesis, so reset the current group
                current_group = ""

    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```
In this solution, we iterate over each character in the input string and build the current group by pushing opening parentheses to the stack and popping them when we encounter a matching closing parenthesis. When we find a complete group (i.e., the stack is empty after popping a closing parenthesis), we add it to the list of separated groups. Finally, we return the list of separated groups.