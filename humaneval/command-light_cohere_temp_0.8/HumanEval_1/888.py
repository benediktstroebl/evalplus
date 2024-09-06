```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses. Return the list of separated groups.
    """
    particular group of balanced parentheses
    and spaces are preserved.
    """
    expected output: [('(', ')'), ('()', '('), '(()')')]
    """
    return [char for char in s if char in '(( )')']
```