```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    This function separates the groups of nested parentheses from the input string.
    Each group of parentheses are separated into separate strings and returned as a list.
    Example:
    - The input string is in the format of nested parentheses.
    - For example, input: `( )((()))`
    - Expected output: [(), ]
    """
    return [c for c in parentheses. ][1::1:]
``` 
This function will take a string of parentheses as input and will return a list of the separated parentheses.