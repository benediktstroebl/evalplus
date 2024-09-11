```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, 
    separates the groups of balanced parentheses, and returns them as a list of strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize an empty list to store the groups of balanced parentheses
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increase the balance
        if char == "(":
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrease the balance
        elif char == ")":
            balance -= 1
            current_group += char

            # If the balance is zero, it means we have a complete group of balanced parentheses
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

When you run this script, it will print `['()', '(())', '(()())']`, which is the expected output.