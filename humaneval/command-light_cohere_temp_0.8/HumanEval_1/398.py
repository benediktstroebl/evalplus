Here is a self-contained Python script that solves the problem of separating out the groups of parentheses in a given string:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate groups of well-formed parentheses.
    Input is string containing multiple groups of parentheses.
    Output: list of separated strings
    """
    return [s.split('() )]
```

The function 'split('()')' in the provided code returns a list of the individual strings by splitting the input string around the open parentheses.

It effectively resolves the problem of separating groups of parentheses by splitting the string into individual components.