```markdown
### Separate Paren Groups
#### Problem Description

This Python script solves the problem of separating multiple groups of nested parentheses into separate strings.

#### Code

```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    - paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    - List[str]: A list of strings where each string represents a group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """

    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Initialize an empty list to store the result
    result = []

    # Initialize an empty string to build the current group
    current_group = ''

    # Initialize a counter to keep track of the balance of parentheses
    balance = 0

    # Iterate over each character in the input string
    for char in paren_string:
        # If the character is an open parenthesis, increment the balance
        if char == '(':
            balance += 1
            current_group += char
        # If the character is a close parenthesis, decrement the balance
        elif char == ')':
            balance -= 1
            current_group += char

            # If the balance is zero, it means we have a complete group
            if balance == 0:
                result.append(current_group)
                current_group = ''

    # Return the list of groups
    return result

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

#### Explanation

This script defines a function `separate_paren_groups` that takes a string `paren_string` as input. It removes spaces from the input string, initializes an empty list `result` to store the result, and an empty string `current_group` to build the current group of parentheses. It also initializes a counter `balance` to keep track of the balance of parentheses.

The function then iterates over each character in the input string. If the character is an open parenthesis, it increments the balance and adds the character to the current group. If the character is a close parenthesis, it decrements the balance, adds the character to the current group, and checks if the balance is zero. If the balance is zero, it means we have a complete group, so it adds the current group to the result list and resets the current group.

Finally, the script returns the list of groups. The example usage demonstrates how to call the function with a sample input string.