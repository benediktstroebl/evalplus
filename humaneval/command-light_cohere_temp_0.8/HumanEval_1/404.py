```python
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """ This function takes a string containing groups of parentheses and returns a list of separate, balanced parentheses.
    : The input is assumed to be free of leading or trailing spaces.
    The balanced parentheses are defined as having exactly two open parentheses, and the closing parentheses.
    """  List[open_braces = ["({", ')(', ')', '[]', '{}']
    open_parents = ''.joinmap(lambda x: x[0], open_braces)
    return [x for x in paren_string.open(open_parents)]
```
This code defines a function named `separate_paren_groups` that takes a string of parentheses as input and returns a list of separate, balanced parentheses. The function uses the leading open parentheses and closing parentheses and creating a new list of parenthesis groups. The final list contains balanced parentheses and doesn't have any leading or trailing spaces.