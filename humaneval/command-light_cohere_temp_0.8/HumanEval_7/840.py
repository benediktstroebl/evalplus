```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests for filter_by_substring function
strings = ["abc", "a", "ace", "b", "buffalo", "cde", "sarah"]
substring = "a"

# Function should return ['abc', 'a', 'ace', 'b']
test_filter_by_substring = filter_by_substring(strings, substring)
 assert test_filter_by_substring == ['abc', 'a', 'ace', 'b']

# Function should return []
test_filter_empty = filter_by_substring([], "x")
 assert test_filter_empty == []
```
This Python script provides a function `filter_by_substring` that filters an input list of strings to include only those that contain a given substring. The unit tests then validate that the function returns the correct results for various inputs.