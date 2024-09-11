```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate those groups into separate strings and return the list of those.
    
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of separate strings of balanced parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all substrings enclosed in parentheses
    groups = re.findall(r'\([^()]+\)', paren_string)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re.findall` function from Python's built-in `re` module to find all substrings that match the pattern of one or more characters enclosed in parentheses. The pattern `r'\([^()]+\)'` is a regular expression that matches:

- A left parenthesis `\(`
- One or more characters that are not parentheses `[^()]+`
- A right parenthesis `\)`