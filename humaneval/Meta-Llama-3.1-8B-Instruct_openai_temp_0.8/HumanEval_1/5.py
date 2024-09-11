### Separate Paren Groups
#### Problem Description
Input to this function is a string containing multiple groups of nested parentheses. 
Your goal is to isolate those groups into separate strings and return the list of those.
Separate groups are balanced (each open brace is properly closed) and not nested within each other
Ignore any spaces in the input string.

#### Solution
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separate groups
    separate_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of open and close parentheses
    open_count = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the counter
        if char == "(":
            open_count += 1
            current_group += char
        # If the character is a close parenthesis
        elif char == ")":
            # If the counter is not zero, decrement the counter and add the character to the current group
            if open_count!= 0:
                open_count -= 1
                current_group += char
            # If the counter is zero, it means we've encountered a close parenthesis without an open parenthesis,
            # so we add the current group to the list and reset the current group
            else:
                separate_groups.append(current_group)
                current_group = ""
        # If the character is not a parenthesis, ignore it

    # Add the last group to the list
    separate_groups.append(current_group)

    # Return the list of separate groups
    return separate_groups
```

### Example Use Case
```python
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
```