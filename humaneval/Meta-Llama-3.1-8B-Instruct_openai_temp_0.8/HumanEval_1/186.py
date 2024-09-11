```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses from a string.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each containing a separate group of nested parentheses.
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')

    # Find all groups of parentheses in the string
    groups = re.findall(r'\([^()]+\)', paren_string)

    return groups

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script first removes any spaces from the input string, then uses a regular expression to find all groups of parentheses. The regular expression `\([^()]+\)` matches any substring that starts with an opening parenthesis, contains one or more characters that are not parentheses, and ends with a closing parenthesis. The `findall` method returns a list of all non-overlapping matches of this regular expression in the string.