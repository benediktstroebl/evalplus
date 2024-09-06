```python
from typing import List
def separate_paren_groups(s: str) -> List[str]:
    """Separate each group of parentheses into separate strings"""
    return [p for p in s.join()]
``` This method takes a string `s` containing multiple groups of parentheses. It uses a `join` to join each pair of parentheses into a single string, and then iterates over this joined string to split it into individual groups of parentheses. The function returns a list of strings, each containing a single open parenthesis.