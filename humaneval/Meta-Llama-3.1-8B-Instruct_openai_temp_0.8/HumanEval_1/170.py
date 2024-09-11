```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
        paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
        List[str]: A list of strings where each string is a separate group of nested parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all balanced groups of parentheses
    # The pattern '\([^()]*\)' matches a '(' followed by any number of non-'(' and non-')' characters
    # and then a ')'. The '?' after '*' makes the match non-greedy.
    groups = re.findall(r'\([^()]*\)', paren_string)

    # Return the list of groups
    return groups

# Example usage:
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re` module's `findall` function to find all balanced groups of parentheses in the input string. The regular expression pattern `'\([^()]*\)'` matches a '(' followed by any number of non-'(' and non-')' characters, and then a ')'. The '?' after '*' makes the match non-greedy, so that it matches the smallest possible substring instead of the largest. The result is a list of strings where each string is a separate group of nested parentheses.