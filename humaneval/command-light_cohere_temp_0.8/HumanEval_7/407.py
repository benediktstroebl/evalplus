Here's a Python script with a self-contained function that filters an input list of strings for those containing a specific substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Testing the function with known correct results
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Verify that the function returns the correct output
print(filter_by_substring(strings, substring))
# Prints ['abc', 'bacd', 'array']
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the given substring. The function uses a Python list comprehension and the `in` operator to achieve this.