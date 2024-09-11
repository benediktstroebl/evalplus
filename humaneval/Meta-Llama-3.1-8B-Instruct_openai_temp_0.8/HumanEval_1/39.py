```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a string and returns them as a list of strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, where each string is a group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the separated groups
    separated_groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter for the opening and closing parentheses
    opening_count = 0

    # Iterate over the input string
    for char in paren_string:
        if char == "(":
            # If we encounter an opening parenthesis, increment the count
            opening_count += 1
            # Add the opening parenthesis to the current group
            current_group += char
        elif char == ")":
            # If we encounter a closing parenthesis, decrement the count
            opening_count -= 1
            # Add the closing parenthesis to the current group
            current_group += char
            # If the count is zero, it means we have a complete group
            if opening_count == 0:
                # Add the current group to the list of separated groups
                separated_groups.append(current_group)
                # Reset the current group and the count
                current_group = ""
                opening_count = 0

    return separated_groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
```

This script works by iterating over the input string and constructing the current group of parentheses by keeping track of the count of opening and closing parentheses. Whenever the count reaches zero, it means we have a complete group, so we add it to the list of separated groups and reset the current group and the count.