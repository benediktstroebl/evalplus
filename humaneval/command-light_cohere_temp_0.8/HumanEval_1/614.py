Here is a self-contained Python script that solves the problem of separating multiple groups of nested parentheses:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    A function to separate and rearrange parentheses appropriately.
    """
    Python string s = s.split(' '())')
   
    return ['(' + item + ')' for item in s.join('')]
```
This script defines a function called `separate_paren_groups`, which takes a string `s` as input and returns a list of strings, each containing a well-formed parenthesis group.  The `split()` is used to split the string `s` into individual parenthesis groups, and then a list comprehension is used to create the string by joining each item back together with the surrounding `')` character.