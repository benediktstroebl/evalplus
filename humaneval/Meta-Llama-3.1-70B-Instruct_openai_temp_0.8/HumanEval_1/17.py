```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a separate group of parentheses.
    """
    paren_string = paren_string.replace(" ", "")  # Remove any spaces from the input string
    groups = []
    temp = ""
    balance = 0

    for char in paren_string:
        temp += char
        if char == "(":
            balance += 1
        elif char == ")":
            balance -= 1
        if balance == 0:  # When the balance is zero, we have a complete group
            groups.append(temp)
            temp = ""

    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```