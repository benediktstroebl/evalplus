```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the length of the longest string in the list.
    """
    # Raises TypeError for non-string input
    if not isinstance(strings, List):
        raise TypeError('Input must be a list')
    # Sort the list to ensure stability and consistent result
    strings.sort()
    _ best to worst: 
    return max(strings, key=len)
    # Sort the list to ensure stability and consistent result
    # reverse to get the original order back
    return max(strings, key=lambda x: len(x[::-1]), default=None)

# Test cases
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 3
strings = ["hello", "hello world", "hello!"]
print(longest(strings))  # Output: 3
strings = ["hello", "world"]
print(longest(strings))  # Output: 2
strings = ["a", "ab"]
print(longest(strings))  # Output: 2
strings = []
print(longest(strings))  # Output: None
```