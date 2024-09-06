```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates balanced parentheses groups into individual strings.
    Returns a example list of strings.
    """
    balanced (each open brace is properly closed) and not nested within each
    other.
    """
    strings"""
    Open and close all balanced parentheses in the input string, without considering extra spaces. The output is a list of separate strings.

Example usage:
```python
input_str = "((()))"
result = separate_paren_groups(input_str)
print(result) # Output: ['()']
```

This function is self-contained and does not require any additional modules. It efficiently separates balanced parentheses into individual strings using a recursive approach.