Here's a Python script that defines a function called `separate_paren_groups`, which accepts a string containing parentheses as an argument and returns a list of separate, balanced groups of parentheses:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """
    Function to separate balanced parentheses from the string.
    Return a string containing separate balanced groups of parentheses.
    """
Input is a string of balanced parentheses
    """
    return [p.strip() for p in parentheses.equal_groups(parentheses)]
```
Do you need assistance with anything else?