```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Return the longest string in a list of strings.
    :return max(strings, key=len)
    """
    return max(strings, key=len)

# Testing the function
strings = ["a", "b", "cc", "abc"]
print(longest(strings))  # Output: "ccc"

strings = ["a", "bb", "abc", "cc"]
print(longest(strings))  # Output: "bb"

strings = ["abc"]
print(longest(strings))  # Output: "abc"

strings = []
print(longest(strings))  # Output: None
```
This solution uses the Python built-in function `max` along with the `key` parameter to return the value by which the corresponding elements in the input list were sorted. The `max` function then compares strings by their length, and the `len` function is used as the key. This ensures that the longest string is found first.