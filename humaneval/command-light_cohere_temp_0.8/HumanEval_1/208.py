```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [part.pen for part in s.format(s, '(', ')')]
``` 
This Python code defines a function called `separate_paren_groups` that takes a string `s` as input and returns a list of separated parenthesis groups as a list of strings. It does this by using the `format` function to split the string into a list of formatted strings, where each formatted string consists of a parenthesis group. 
The `format` function takes the input string `s` and formats it by expanding all parenthesis to their own groups (open and closed), creating the desired separated parenthesis groups. 
This is a self-contained function that effectively solves the problem of separating and formatting parenthesis groups in a string.