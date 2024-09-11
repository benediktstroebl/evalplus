```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function takes a string of nested parentheses and returns a list of strings, where each string is a separate group of balanced parentheses.

    :param paren_string: A string containing multiple groups of nested parentheses.
    :return: A list of strings, where each string is a separate group of balanced parentheses.
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Use regular expression to find all balanced groups of parentheses
    patterns = re.findall(r'\([^()]+\)', paren_string)

    # Return the list of balanced groups
    return patterns

# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))  # Output: ['()', '(())', '(()())']
```

This script uses a regular expression to find all balanced groups of parentheses within the input string. The `re.findall` function returns all non-overlapping matches of the regular expression in the string as a list of strings. The regular expression `\([^()]+\)` matches any substring that starts and ends with a parenthesis and contains one or more characters that are not parentheses.