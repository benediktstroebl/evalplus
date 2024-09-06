```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the length of the longest string.
    """
    strings = [str.strip() for str in strings]
    max_length = max(len(str) for str in strings)
    return max_length if max_length is not None else None

# Test cases
assert longest(['a', 'b', 'c']) == 3
assert longest(['a', 'bb', 'ccc']) == 3
assert longest([]) == 0
assert longest(['aa', 'a']) == 1
assert longest(['a', 'b', 'ccc']) == 3
```
The above Python script defines a function called longest, which accepts a list of strings as input and returns the length of the longest string in the list. It utilizes the max function to find the maximum length of the string, and returns the length if it is not None; In the test cases section, the function is tested with various input strings to ensure it behaves correctly.