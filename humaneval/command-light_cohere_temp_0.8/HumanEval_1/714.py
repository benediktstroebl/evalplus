Here is a Python script that defines a function named `separate_paren_groups` that solves the problem of separating multiple groups of parentheses into individual strings:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Function to separate and organize parentheses into individual strings.
    - Returns input string containing multiple groups of parentheses.
    - Separate groups of parentheses, each with balanced open and close braces.
    - Returns the separated strings without any nesting or extra spaces
    Input: string of parentheses
    Output: list of separated strings"""
    return [eval(p) for p in s.p]
```
def eval(s):
    return s.replace('()', r'() for r in ["[]", "())"])
```

This function takes an input string s composed of multiple groups of parentheses and returns a list of separated strings. The `eval` function is used to convert the parentheses string into a valid format for the `separate_paren_groups` function. 

Please note that this script is self-contained and can be used as-is with no additional imports or external functions.