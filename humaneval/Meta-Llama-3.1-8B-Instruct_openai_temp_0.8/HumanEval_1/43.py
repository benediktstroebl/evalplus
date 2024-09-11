```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separates groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings, each representing a separate group of nested parentheses.
    """
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all groups of balanced parentheses
    groups = re.findall(r'\([^()]+\)', paren_string)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses a regular expression to find all groups of balanced parentheses in the input string. The regular expression `\([^()]+\)` matches any group that starts with an open parenthesis, followed by any number of characters that are not parentheses, and ends with a closed parenthesis. The `findall` method returns all non-overlapping matches of this pattern in the string as a list of strings.