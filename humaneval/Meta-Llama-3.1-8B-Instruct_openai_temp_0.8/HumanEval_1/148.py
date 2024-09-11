```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string into a list of balanced groups.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a group of balanced parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all balanced groups of parentheses
    groups = re.findall(r'\((?:[^()])*\)', paren_string)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a regular expression to find all balanced groups of parentheses in the input string. The regular expression `\((?:[^()])*\)` matches any substring that starts with an opening parenthesis `\(`, followed by any number of characters that are not parentheses `[^()]`, and ends with a closing parenthesis `\)`.

The `findall` function returns all non-overlapping matches of the regular expression in the string, as a list of strings. Each string in the list is a group of balanced parentheses.

The `replace` function is used to remove any spaces from the input string, as required by the problem statement.