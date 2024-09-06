Here's a self-contained Python script that defines a function `filter_by_substring` that filters an input list of strings based on a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Testing the function
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This code provides a complete, self-contained solution to the problem. You can use this simply copy-and-paste this Python script into your Python environment, and then call the `filter_by_substring` function with your input strings and substring to get the desired output.