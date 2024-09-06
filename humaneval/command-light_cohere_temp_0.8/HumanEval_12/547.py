```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, return the longest one.
    """
    max_length = max([len(str) for str in strings])
    return max([str[0:max_length] for str in strings]) or None

# Tests
strings = ["a", "b", "bb", "ccc", "apple"]
print(longest(strings))  # Output: "ccc"

strings = ["a", "b", "bb", "apple", "asdf"]
print(longest(strings))  # Output: "apple"

strings = []
print(longest(strings))  # Output: None

strings = ["python", "is", "language"]
print(longest("pylang"))  # Output: "is"
```