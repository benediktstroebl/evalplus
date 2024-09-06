Here is a Python script with a self-contained function that solves the problem of separating multiple groups of parentheses into separate strings:
```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """
    Separates groups of parentheses into separate strings.
    """
    balanced (each open brace is properly closed) and not nested within each other.
    Returns a More list of those separated strings.
    """
    separated(s, lambda x: x.p == x.group('()', lambda x: x.p == '('))
    return ['(') + s.group(x(') + s[1:] + '(')]
```
The function `separate_paren_groups` takes a string `s` as input and returns a list of strings. The function uses the balanced parentheses and returns a list of those separated strings.