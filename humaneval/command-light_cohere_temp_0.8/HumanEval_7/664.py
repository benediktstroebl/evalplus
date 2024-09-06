Here is a self-contained Python script with a function that filters an input list of strings for those containing a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
# Test cases
strings = ["abc", "bacd", "cde", "array", "hello world"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This script provides a function `filter_by_substring` that filters an input list of strings based on whether the given substring exists within each string. 
It uses a list comprehension to iterate over the strings and checks if the substring is present.