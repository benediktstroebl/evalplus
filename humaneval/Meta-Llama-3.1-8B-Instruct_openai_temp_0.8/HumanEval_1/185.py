```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses from a given string.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each containing a separate group of balanced parentheses.

    Examples:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Find all groups of parentheses using a regular expression
    groups = re.findall(r'\([^()]+\)', paren_string)
    
    # Return the list of groups
    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re` module in Python, which provides regular expression matching operations. The regular expression `\([^()]+\)` matches any substring that starts with an open parenthesis, contains one or more characters that are not parentheses, and ends with a close parenthesis. The `findall` method returns all non-overlapping matches of this regular expression in the string as a list of strings.