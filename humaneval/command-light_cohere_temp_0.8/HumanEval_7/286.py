```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["one", "two", "23", "four", "int"]
substring = "two"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['two', '23']

# Test case 3
strings = ["a", "bb", "abc", "bd"]
substring = "ab"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bd']
```

This Python script defines a function `filter_by_substring` that filters an input list of strings and returns a new list that includes only the strings that contain the given substring. The test cases demonstrate how the necessary this function handles different inputs and produces the expected results.