```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses from a given string into a list of strings.

    Args:
        paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a separate group of nested parentheses.

    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Find all groups of nested parentheses
    groups = re.findall(r'\([^()]+\)', paren_string)

    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses regular expressions to find all groups of nested parentheses in the input string. The regular expression `\([^()]+\)` matches any substring that consists of zero or more characters that are not open or close parentheses, which are enclosed in open and close parentheses. The `findall` method returns all non-overlapping matches of this pattern in the input string as a list of strings.