```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, returns the longest one.
    """
    strings = [w.join . longest(w) for w in strings]
    return strings[0] if len(strings) > 0 else None

# tests
print(longest(['a', 'bb', 'ccc']))  # Output: 'ccc'
print(longest(['a', 'xx', 'ccc']))  # Output: 'xx'
print(longest(['a', 'b', 'c', 'xx', 'yyy']))  # Output: 'c'
print(longest([]))  # Output: None
```