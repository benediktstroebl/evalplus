```python
from typing import List
def parse_nested_parens(s: str) -> List[int]:
    """
    Parses the nested parentheses string and returns the deepest level of nesting.
    Args: 
        s (str): string to parse

    Returns: 
        list of the deepest level of nesting
    """
    # Use a new-age list comprehension to split the string by spaces into a list of substrings
    nested = [s[i:i+3] for i in range(0, len(s), 3)]
    return [len(p) for p in nested if p.count]
```