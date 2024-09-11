### Separate Parenthesis Groups
#### Python Script to Separate Parenthesis Groups

```python
from typing import List
import re

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    This function separates balanced groups of nested parentheses in a string into separate strings.

    Args:
    paren_string (str): A string containing multiple groups of nested parentheses.

    Returns:
    List[str]: A list of strings where each string represents a balanced group of parentheses.

    Example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    
    # Remove any spaces from the input string
    paren_string = paren_string.replace(" ", "")

    # Find all balanced groups of parentheses in the string
    groups = re.findall(r'\([^()]*\)', paren_string)

    return groups
```

### Example Use Case

```python
print(separate_paren_groups('( ) (( )) (( )( ))'))
# Output: ['()', '(())', '(()())']
```

This Python script defines a function `separate_paren_groups` that takes a string of balanced groups of nested parentheses as input. The function removes any spaces from the input string, uses a regular expression to find all balanced groups of parentheses, and returns a list of these groups.