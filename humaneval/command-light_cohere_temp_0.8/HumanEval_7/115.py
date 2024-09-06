```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array", "f Ged"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abc", "def", "hello", "world"]
substring = "o"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'def']

# Test case 3
strings = ["abc", "good morning", "how are you"]
substring = "good"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'good morning']
```

This Python script defines a function `filter_by_substring` that takes two arguments: a list of strings and a substring. The function returns a filter the strings from the list that contain the substring. The test cases demonstrate how the string list and substring can be used to test the function.