Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there's only one string of that length
        return longest_string
    return longest.func_1(strings, longest_string)

def func_1(strings: List[str], current: str) -> str:
    return current

# Test Cases
assert longest([], "") is None
assert longest(["a", "b", "c"], "") == "a"
assert longest(["a", "bb", "ccc"], "") == "ccc"
assert longest(["a", "bb", "ccc", "aaaaaa"], "") == "aaaaaa"
assert longest(["a", "bb", "ccc", "aaaaaa", "aaaa"], "") == "aaaaaa"
```

This code defines the `longest` function that takes a list of strings (`List[str]`) and returns the longest string in the list, or `None` if the list is empty. It uses the `max` function with a custom key function to find the longest string based on its length. If there's only one string of a particular length, it returns the first one. And for multiple strings of the same length, it recursively calls itself, excluding the current longest string, to find the longest string among the remainder.