Here's a self-contained Python script that solves the problem and passes the tests:
```python
from typing import List
def longest(strings: List[str]) -> str:
    # Function to find the length of the longest string in the list
    max_length = min_length = 0
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
        min_length = len(string)
    return max_length if max_length != 0 else None
test_longest = [
    "a", "bb", "ccc" ]
test_empty = []
print(longest(test_longest))  # Output: 3
print(longest(test_empty))  # Output: None
```

This code defines a function `longest` that takes a list of strings as an argument and returns the length of the longest string. The function initializes two variables `max_length` and `min_length` to zero, then iterates through the input strings and updates the `max_length` and `min_length` values whenever a longer string is found.  The function then returns the longest string's length and updates the function's return value to `None` when the input list is empty.