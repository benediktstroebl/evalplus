```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and separates these groups into separate strings, maintaining balanced parentheses.
    :s has no nested or balanced parentheses
    :return: A list of strings, each representing a properly formatted group of parentheses.
    """
Example usage:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    result = []
    balance = 1
    for char in s:
        if char == ' ':
            balance += 1
        elif balance > 0:
            balance -= 1
        else:
            result.append(char)
    return result
```
This code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of strings. The function uses a balanced parentheses and nested groups by keeping a counter called balance. It iterates over each input string and checks if the current character is a space. The function maintains the balance by either adding or subtracting 1 from the balance depending on the character's value.