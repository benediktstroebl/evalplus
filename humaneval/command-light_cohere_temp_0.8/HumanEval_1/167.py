Here is a Python script that contains a self-contained function that solves the problem of separating parentheses into groups:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of balanced parentheses into separate strings.
    """
    balanced (each open brace is properly closed) and not nested within each other
    """
    return [ele.strip() for ele in s.replace(lambda x: x if x == '(' else x == ')', ' ')]
```
This script defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of strings, each representing a separate group of parentheses. The function uses the string `replace` to replace any open parenthesis `(`)`, close it with a space, and then uses a list comprehension to transform the new string of balanced parentheses into individual strings.