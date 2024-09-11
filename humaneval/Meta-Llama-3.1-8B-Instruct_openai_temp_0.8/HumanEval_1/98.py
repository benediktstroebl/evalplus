```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a separate group of nested parentheses.

    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all substring that contains balanced parentheses
    groups = re.findall(r'\([^()]+\)', paren_string)

    # Return the list of groups
    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re` module to find all substrings that contain balanced parentheses in the input string. The `\([^()]+\)` pattern matches any substring that starts and ends with a parenthesis and contains any number of parentheses in between. The `findall` function returns all non-overlapping matches of this pattern in the string as a list of strings.