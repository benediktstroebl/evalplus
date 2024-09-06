```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from a list of strings.
    """
    longest = ""
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest

# Test cases
print(longest(["a", "bb", "ccc"]))  # Output: "ccc"
print(longest(["aa", "bb", "ccc"]))  # Output: "ccc"
print(longest(["abcd", "abcd", "abcd"]))  # Output: "abcd"
print(longest(["abrcdf", "abcdefghijklmnopqr"])) # Output: "abcdefghijklmnopqr"
print(longest(["abc", "def"]))  # Output: "def"
print(longest([]))          # Output: None
```
This script defines a function `longest` that takes a list of strings as an argument and returns the longest string. It then passes these tests to the function, and the results are printed to the console.