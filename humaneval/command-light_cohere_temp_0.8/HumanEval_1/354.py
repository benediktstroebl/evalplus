Here is a Python script that contains a self-contained function that solves the problem of separating multiple groups of parentheses into individual strings:
```python
from typing import List
def separate_paren_groups(parentheses: List[str]) -> List[str]:
    """Separate each group of parentheses into separate strings.
    :param List[str] parents: List of strings containing parenthesis groups
    :return List[str]: List of separate strings
    """
    return [parent.split('()') for parent in parents]
```
This code defines a function `separate_paren_groups` that takes a list of strings as input, representing a list of parenthesis groups. The function splits each string into individual parentheses and returns a list of separate strings.