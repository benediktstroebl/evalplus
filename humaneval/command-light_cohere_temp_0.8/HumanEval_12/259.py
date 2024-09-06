```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Returns the length of the longest string in the list.
    """
    list of strings = sorted(strings, key=len, reverse=True)
    return max(list, key=len)

# Test cases
print(longest(['a', 'bb', 'ccc']))  # Output: 3
print(longest(['abc', 'abc', 'ABC']))  # Output: 3
print(longest(['ab']))  # Output: 2
print(longest(['abcde', 'abcd']))  # Output: 4
```
This Python script defines a function named `longest` that takes a list of strings as input and returns the length of the longest string. The function sorts the string list in descending order based on their lengths, then returns the length of the longest string using the `max` function. The test cases demonstrate the example of passing different strings to the function and expect the correct output.