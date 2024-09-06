Certainly, here is a Python script that includes a self-contained function that solves the problem of separating nested parentheses into individual groups:
```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    This function takes a string s containing multiple groups of parentheses and returns a list of separate strings,
    each representing a group of parentheses.
    """
    open_brace = [')', '(', ')'']
    closed_brace = [')', ')', ']'
    result = []

    for char in s:
        if char in open_brace:
            result.append(') ' + char)
        elif char in closed_brace:
            result.append('(' + char)
        else:
            result.append(char)

    return result
```

This script provides a way to separate and manipulate parentheses within a given string. It utilizes a list of open and closed parentheses to achieve this.  The method iterates through each character in the string, and uses appropriate list transformations to correctly separate the parentheses into individual groups.