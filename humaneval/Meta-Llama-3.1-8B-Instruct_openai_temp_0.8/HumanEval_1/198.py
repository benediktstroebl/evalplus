```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates groups of nested parentheses in a given string into separate strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings, each representing a group of separated parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    # Remove spaces from the input string
    paren_string = paren_string.replace(' ', '')
    
    # Use regular expression to find all balanced groups of parentheses
    # The pattern '\(.*?\)' matches any substring that starts and ends with '(' and ')'
    # The '?' after '*' makes the match non-greedy, so it stops at the first ')' it encounters
    groups = re.findall(r'\(.*?\)', paren_string)
    
    # Return the list of groups
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script uses the `re` module in Python, which provides support for regular expressions. The regular expression pattern `\(` and `\)` are used to match the opening and closing parentheses, and `.*?` is used to match any characters (including none) between them. The `findall` method returns all non-overlapping matches of the pattern in the string as a list of strings.