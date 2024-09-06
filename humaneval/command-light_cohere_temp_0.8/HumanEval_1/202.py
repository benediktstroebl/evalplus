Here is a self-contained Python script that includes the function `separate_paren_groups` which solves the problem you provided:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups in balanced parentheses and return the list of separated strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    return [p.strip() for p in parentheses_to_string(parentheses)]
def parentheses_to_string(parentheses: str) -> str:
    """
    Input is a string containing groups of parentheses.
    Return a string containing only the spaces between the parenthesis"""
    return ' '.join(parentheses.replace('()', ' '))
```
This script includes the function `separate_paren_groups` that takes a string of parentheses as input and returns a list of separated parenthesis strings. The function `parentheses_to_string` is used to transform the input into a string of spaces-separated parenthesis.