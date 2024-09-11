```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a close parenthesis, add it to the current group and check if the group is complete
        elif char == ")":
            current_group += char
            # If the group is complete, add it to the result list and reset the current group
            if len(current_group) >= 2 and current_group.count("(") == current_group.count(")"):
                result.append(current_group)
                current_group = ""

    # Return the list of separate groups
    return result


# Example usage
if __name__ == "__main__":
    print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a simple iterative approach to separate the groups of parentheses. It keeps track of the current group being built and adds it to the result list when it encounters a closing parenthesis that completes a group. The script ignores spaces in the input string and returns a list of separate groups as required.