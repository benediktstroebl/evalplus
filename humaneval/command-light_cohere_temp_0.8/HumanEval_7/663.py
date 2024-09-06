```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Example usage:
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This code defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring.  The filter function uses a built-in `List[str]` function and a `for` loop to iterate through each string in the input list.