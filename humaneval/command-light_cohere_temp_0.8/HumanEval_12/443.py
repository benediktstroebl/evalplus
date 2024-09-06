Here is a self-contained Python script that defines a function `longest()` which returns the longest string from a list of strings:

```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Find the length of the longest string.
    """
    max_len = min(len(strings), key=len)
    return strings[max_len]

# Test the function with various lists of strings
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'
assert longest([]) is None
```

Please feel free to use this script and let me know if you need any further assistance.