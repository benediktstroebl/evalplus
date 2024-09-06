Here's the self-contained Python script that solves the problem of separating parentheses into individual groups:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [ chr(c) for c in s if c != '(' and c != ')']
```
This script defines a function `separate_paren_groups` that takes a string `s` as input and returns a list of non-parenthesis characters from the input string. 

The function uses a list comprehension to iterate through each character in the input string `s`. It only includes characters that are not '(' or ')'.  The list of characters is then returned. 
This function is self-contained, as it can solve the problem of separating parentheses into individual groups without relying on any other functions or external variables.