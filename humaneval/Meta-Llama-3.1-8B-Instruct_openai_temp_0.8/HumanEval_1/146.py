```python
import re
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested balanced parentheses in a string into separate strings.
    
    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.
    
    Returns:
        List[str]: A list of strings, each representing a separate group of balanced parentheses.
    """
    
    # Remove leading and trailing spaces from the input string
    paren_string = paren_string.strip()
    
    # Use regular expression to find all groups of balanced parentheses
    groups = re.findall(r'\([^()]+\)', paren_string)
    
    return groups


# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re` module's `findall` function to find all substrings that consist of `(`, followed by any number of characters that are not `(` or `)`, and finally a `)`. These substrings represent the separate groups of balanced parentheses. The function then returns a list of these substrings.