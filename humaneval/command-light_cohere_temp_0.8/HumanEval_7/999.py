Here is a self-contained Python script with a function that filters an input list of strings for a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "edcba"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print the result
print(result)
```
The code defines a function `filter_by_substring` that takes a list of strings and a substring as input, and returns a new list containing only the strings that contain the given substring. The test cases demonstrate the
that the function correctly filters the input strings for the given substring.