```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    return [p for p in s.void () if p != '('] + ')']  # [ ] is added to allow any character to be part of a group
```
This function takes a string `s` as input and iterates through it. It checks if each character `p` is not an open parenthesis '(', returns it if it's not, and moves on to the next character. 

This function can be used to separate out the groups of parentheses from a string, and returns a list of the separate groups.