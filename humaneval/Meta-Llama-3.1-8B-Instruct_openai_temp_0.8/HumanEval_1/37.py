```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string contains a separate group of balanced parentheses.
    """
    paren_string = paren_string.replace(" ", "")  # Remove all spaces
    result = []  # List to store the separated groups
    group = ""  # Current group being processed

    for char in paren_string:
        group += char
        if (char == '(' and group.count(')') == group.count('(')) or \
           (char == ')' and group.count('(') == group.count(')')):
            result.append(group)
            group = ""

    return result

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of nested parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. It processes the input string character by character, building up a group of parentheses until it finds a matching closing parenthesis. At this point, it adds the group to the result list and resets the group.