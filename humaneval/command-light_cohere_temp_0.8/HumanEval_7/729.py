```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'xzyx']
substring = 'a'
result = filter_by_substring(strings, substring)
print(result)  # Output ['abc', 'bacd', 'array']
```
This Python script defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function uses a string method `in` to check if each string contains the given substring. The test cases demonstrate the for different scenarios, and the output will be the list of strings that contain the specified substring.