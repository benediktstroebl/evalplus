```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input and returns a list of strings, 
    where each string is a separate group of balanced parentheses.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings, where each string is a separate group of balanced parentheses.
    """
    
    # Remove spaces from the input string
   (paren_string := paren_string.replace(" ", ""))

    # Initialize an empty list to store the separate groups
    groups = []

    # Initialize an empty string to build the current group
    current_group = ""

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over the characters in the input string
    for char in paren_string:
        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
            current_group += char

        # If the character is a closing parenthesis, decrement the balance
        elif char == ")":
            balance -= 1
            current_group += char

            # If the balance is zero, it means we have found a complete group
            if balance == 0:
                groups.append(current_group)
                current_group = ""

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```