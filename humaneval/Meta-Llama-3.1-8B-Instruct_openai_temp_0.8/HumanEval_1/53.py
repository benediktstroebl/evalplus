```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of balanced parentheses from a given string.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of balanced parentheses.
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # Find all groups of balanced parentheses using regular expression
    groups = re.findall(r'\([^()]+\)', paren_string)
    
    return groups

# Example usage
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

In this script, we're using the `re` (regular expression) module in Python to find all occurrences of balanced parentheses in the input string. The regular expression `\([^()]+\)` matches any substring that starts and ends with a parenthesis and contains only parentheses and possibly other characters in between. The `findall` function returns all non-overlapping matches of this regular expression in the string as a list of strings.