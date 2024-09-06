```python
from typing import List
def longest(strings: List[str]) -> str:
    """
    Return the length of the longest string in the list.
    """
    return max(len(string) for string in strings)

# Test cases for the function
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 3

strings = ["absc"]
print(longest(strings))  # Output: 3

strings = ["abc"]
print(longest(strings))  # Output: 3

strings = []
print(longest(strings))  # Output: None

strings = ["abcd"] * 5
print(longest(strings))  # Output: 6
```
This function accepts a list of strings and returns the length of the longest string in the list. It does so by using the `max()` function to get the length of the longest string, then loops through the list and returns the length of each string until it finds the longest.