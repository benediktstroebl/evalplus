```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses as input, 
    separates them into balanced groups and returns a list of strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string is a balanced group of parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Initialize variables to keep track of the result and the current group
    result = []
    current_group = ""
    balance = 0

    # Iterate over each character in the string
    for char in paren_string:
        # Add the character to the current group
        current_group += char

        # If the character is an opening parenthesis, increment the balance
        if char == "(":
            balance += 1
        # If the character is a closing parenthesis, decrement the balance
        elif char == ")":
            balance -= 1

        # If the balance is zero, it means we have a complete group
        if balance == 0:
            # Add the current group to the result and reset the current group
            result.append(current_group)
            current_group = ""

    return result


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

In this script, we iterate over the input string and use a balance variable to keep track of the nesting level of the parentheses. When the balance is zero, it means we have a complete group, so we add it to the result list and reset the current group. Finally, we return the list of balanced groups.