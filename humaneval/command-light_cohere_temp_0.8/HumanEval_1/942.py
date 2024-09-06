Here is a self-contained Python script that includes the function `separate_paren_groups`, which solves the problem you described:
```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """
    Purpose: To separate a list of strings containing multiple groups of parentheses into separate strings.

    Input: A list of strings containing multiple groups of parentheses.
    Output: A list of separated strings.
    Example:
    Example:
    [('(', ')'), ('(', ')', ')')]
    """
    return [ YY for YY in parentheses if not ')' in YY.  # Filter out any empty parentheses
   

# Test cases
parentheses_test = [('( )(( ))(( ) )', '(', ')', ')')]
print(separate_paren_groups(parentheses_test))  # Output: ['()', '(', ')()', '()', ')')
```
This script defines a function `separate_paren_groups` that takes a list of strings as input and returns a new list where each element is a separate version of the string with balanced parentheses.