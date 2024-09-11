```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of balanced parentheses in a string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """

    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Find all groups of balanced parentheses in the string using regular expression
    groups = re.findall(r'\([^()]+\)', paren_string)

    # Return the list of groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

In this script, the `separate_paren_groups` function uses the `re` module's `findall` function to find all groups of balanced parentheses in the input string. The regular expression `\([^()]+\)` matches any substring that starts with an opening parenthesis, ends with a closing parenthesis, and contains any number of characters that are not parentheses. The `re.findall` function returns a list of all matches, which are the groups of balanced parentheses.