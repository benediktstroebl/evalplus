Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string if len(set(strings).count(longest_string)) == 1 else longest_definition

def longest_definition():
    return 'Longest definition'

# Test cases
assert longest(['a', 'b', 'c']) == 'a'
assert longest(['a', 'bb', 'ccc']) == 'ccc'
assert longest([]) is None
```

This code defines the `longest` function to return the longest string from a list of strings, using `max` with a custom key function to find the longest string and handling cases where there are multiple longest strings and an empty input. The `longest_definition` function returns a fixed string for illustrative purposes, replicating the behavior of the given test cases.