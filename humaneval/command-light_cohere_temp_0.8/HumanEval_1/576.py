```python
from typing import List

def separate_paren_groups(s: str) -> List[str]:
    """
    Function to separate and rearrange groups of parentheses.
    >>> return [map(lambda x: x.open(), s.flatten())
    Meanwhile, match(r"\((.*?)\)", r"\((.*?)\)")[::-1])
    """
    return list(map(lambda x: x.open(), s.flatten()))
```