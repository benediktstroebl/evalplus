```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]


# Test case 1
strings = ["abc", "bcd", "cde", "array", "hello"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output ['abc', 'array']

# Test case 2
strings = ["def", "code", "Enable"]
prefix = "a"
result = filter_by_prefix(strings, prefix)
print(result)  # Output ['def', 'code', 'Enable']
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses thel list comprehension to iterate through the input strings and filter those that start with the specified prefix.