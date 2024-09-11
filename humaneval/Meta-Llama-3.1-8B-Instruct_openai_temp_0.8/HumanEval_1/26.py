```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate groups of nested parentheses into individual strings.

    Args:
    paren_string (str): Input string containing multiple groups of nested parentheses.

    Returns:
    List[str]: List of strings where each string is a separate group of nested parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    import re
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    # Use regular expression to find all substrings enclosed in parentheses
    groups = re.findall(r'\([^()]*\)', paren_string)
    return groups


# Test the function
print(separate_paren_groups('( ) (( )) (( )( ))'))
```

This script defines a function `separate_paren_groups` that takes a string of parentheses as input and returns a list of strings where each string is a separate group of nested parentheses. The function uses regular expressions to find all substrings enclosed in parentheses and returns them as a list. The test at the end of the script demonstrates how to use the function and prints the expected output.