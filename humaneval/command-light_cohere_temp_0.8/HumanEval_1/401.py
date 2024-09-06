Here is a Python script that contains a self-contained function `separate_paren_groups`, which takes a string containing multiple groups of parentheses as input and returns a list of strings that have each group of parentheses properly separated:
```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Separate groups of parentheses into separate strings.
    >>> separate_paren_groups(') ((())) (( )( ))')
        ['(', ')', '()', '()()']
    """
    return [')'.join(p) for p in s.join('(', ')')]
```