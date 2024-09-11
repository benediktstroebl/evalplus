```markdown
### Separate Parenthesis Groups

This script separates groups of nested parentheses into individual strings.

#### Code
```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of individual strings, each containing a separate group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize a list to store the separated groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, add it to the current group
        if char == "(":
            current_group += char
        # If the character is a close parenthesis, add it to the current group and add the group to the list
        elif char == ")":
            current_group += char
            groups.append(current_group)
            current_group = ""

    # Return the list of separated groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

#### Explanation

This script works by iterating over each character in the input string. When it encounters an open parenthesis, it adds it to the current group. When it encounters a close parenthesis, it adds it to the current group and adds the current group to the list of groups. At the end of the script, the list of separated groups is returned.

This script assumes that the input string will always contain balanced and non-nested groups of parentheses. If the input string may contain unbalanced or nested groups, additional error checking would be necessary.