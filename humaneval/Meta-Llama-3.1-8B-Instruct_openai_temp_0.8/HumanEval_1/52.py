```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string contains a separate group of nested parentheses.

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Find all groups of parentheses using regular expression
    groups = re.findall(r'\([^()]+\)', paren_string)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

In this script, we use the `re.findall()` function from Python's built-in `re` (regular expression) module to find all groups of parentheses in the input string. The regular expression `\([^()]+\)` matches any substring that starts with an opening parenthesis, contains one or more characters that are not parentheses, and ends with a closing parenthesis. The `findall()` function returns all non-overlapping matches of this pattern in the string as a list of strings.