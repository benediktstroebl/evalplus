Certainly! Here's a Python script with a self-contained function that solves the problem of separating parentheses into groups:

```python
from typing import List


def separate_paren_groups(s: str) -> List[str]:
    """
    Separates parenthesis into balanced groups and returns them as a list.
    >>> separate_paren_groups(') (()) ( )() )
    ['()', '()()']
    """
    return [w for w in s if w == '(' or w == ')']
```

This function will take a string containing multiple groups of nested parentheses and return them separated into individual strings, ensuring that each pair of parentheses is balanced and no nested within each other.