```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. 

The function uses a list comprehension to iterate over each string in the input list and checks if the given substring exists in the string.