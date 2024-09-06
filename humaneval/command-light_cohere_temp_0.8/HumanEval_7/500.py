```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print the result
print(result)
```
This code defines a function `filter_by_substring` that filters an input list of strings and returns a new list containing only the strings that contain a given substring. It then tests this strings and the substring and prints the result.