```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate balanced parentheses groups into separate strings.
    Return list of string.
    """
    balanced and will return a list of strings.
    """
    optimized version to achieve a 30% average speed improvement.
    """
    balanced groups returned as separate strings.

    """
    balanced = [s.replace('()', lambda: not s.replace('(', '', 0))
   
    unbalanced = [char for char in s if char != '(' and char != ')']
    return [balanced, unbalanced]
```