Here is a self-contained Python script that defines a function to solve the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string.
    """
    required_ list of strings
    longest = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string
    return longest

# Test cases
strings = ["a", "b", "c"]
print(longest(strings))  # Output: 'c'

strings = ["aa", "bb", "ccc"]
print(longest(strings))  # Output: 'ccc'

strings = []
strings. strings long_string = "amazing"
print(longest(strings))  # Output: 'amazing'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. The function compares the longest string with all other strings in the list and keeps updating the longest string until a new longer string is found.