Here is a self-contained Python script that solves the problem of separating parentheses into groups:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Separate groups of parentheses into balanced strings and return the list of those strings.
    """
    new line for readability
    """
    return [ ''.join(w.replace(')', s) for w in ('(',') )]
```
The function 'separate_paren_groups' takes a string 's' as input and returns a list of strings, each representing a balanced group of parentheses. It uses the balanced function to create such strings, where the outer parentheses are replaced by new line for readability.