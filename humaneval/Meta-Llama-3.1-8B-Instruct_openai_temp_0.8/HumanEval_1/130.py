```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of separate strings, each containing a group of balanced parentheses.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Find all groups of balanced parentheses using regular expression
    patterns = re.findall(r'\([^()]+\)', paren_string)

    return patterns

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re.findall()` function from Python's built-in `re` module to find all occurrences of a pattern in the input string. The pattern `\([^()]+\)` matches any substring that starts with a `(`, followed by one or more characters that are not `(` or `)`, and ends with a `)`. The `re.findall()` function returns a list of all matches, which are the separate groups of balanced parentheses.