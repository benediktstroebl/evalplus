```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string containing multiple groups of parentheses and returns a list of separated parenthesis strings.
    """
    Requires the ** balanced (each open brace is properly closed) and not nested within each other.
    Ignores any spaces in the string.
    """
    uses list comprehension to iterate through all the character groups that are not whitespace.
    Returns: list of separated parenthesis strings.
    """
    is a example:
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    return [c for c in s if c != ' ']
```