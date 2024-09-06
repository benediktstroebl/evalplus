```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate balanced parentheses groups into individual strings and return the list.
    >>> '()' == '('.group()(')')
   
    ['()']
    """
    return [s[i:i+2] for i in range(0, len(s), 2)]
``` 
This script's function, `separate_paren_groups`, takes a string `s` as input and returns a list of strings. It uses slicing to find the minimum 2-character span for each group of parentheses, which are returned as a list.