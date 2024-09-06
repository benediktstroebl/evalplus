```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Testing the filter_by_prefix function
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output: ['abc', 'array']
```
This code defines a function `filter_by_prefix` that takes two arguments: a list of strings `strings` and a prefix `prefix`. The function returns a new list containing only the strings from the input list that start with the specified prefix. The provided test cases successfully pass with the expected output.