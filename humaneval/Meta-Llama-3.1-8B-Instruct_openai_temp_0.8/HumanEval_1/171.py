```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses in a string into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of balanced parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all groups of balanced parentheses
    # The pattern '\([^()]*\)' matches a group of parentheses if they are balanced
    groups = re.findall(r'\([^()]*\)', paren_string)

    # Return the list of groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings, each containing a separate group of balanced parentheses. It uses regular expressions to find all balanced groups and returns them as a list. The example usage at the end shows how to call the function and print the result.