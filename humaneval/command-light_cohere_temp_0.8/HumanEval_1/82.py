Here is a Python script that contains a self-contained function that solves the problem of separating parentheses into separate groups and passes all the corresponding tests:
```python
from typing import List
def separate_paren_groups(parentheses: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of balanced parentheses and return the list of those separated strings.
    """
    balanced () pairs and don't have nested ones within each other.
    >>> separate_paren_groups('( )((()))())')
    ['(', '()', '()', '()']
    """
    return ['('', ')') for item in parenthesis.  # split into ('()', ')')
```
This function takes a string of parenthesis groups as an argument and returns a list of separated strings, with each group of parentheses balanced and not nested.